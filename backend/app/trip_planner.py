from sqlalchemy.orm import Session
from . import models, ai_service

STEPS = {
    "STARTING_CITY": "From where will you start your journey?",
    "DESTINATION_CITY": "Where do you want to travel?",
    "DAYS": "How many days is your trip?",
    "VIBE": "What is your travel vibe? (adventure / peace / luxury / culture)",
    "BUDGET": "What is your budget for the trip?",
    "PEOPLE": "How many travelers are going?",
    "COMPLETED": "Perfect! I have all the details for your trip. Generating your itinerary now..."
}

STEP_ORDER = ["STARTING_CITY", "DESTINATION_CITY", "DAYS", "VIBE", "BUDGET", "PEOPLE", "COMPLETED"]

def get_or_create_state(db: Session, user_id: int):
    state = db.query(models.TripPlannerState).filter(models.TripPlannerState.user_id == user_id).first()
    if not state:
        state = models.TripPlannerState(user_id=user_id, current_step="STARTING_CITY")
        db.add(state)
        db.commit()
        db.refresh(state)
    return state

def handle_chat(db: Session, user_id: int, message: str):
    state = get_or_create_state(db, user_id)
    
    current_step = state.current_step
    
    # Map message to fields
    if current_step == "STARTING_CITY":
        state.source = message
        state.current_step = "DESTINATION_CITY"
    elif current_step == "DESTINATION_CITY":
        state.destination = message
        state.current_step = "DAYS"
    elif current_step == "DAYS":
        state.days = message
        state.current_step = "VIBE"
    elif current_step == "VIBE":
        state.vibe = message
        state.current_step = "BUDGET"
    elif current_step == "BUDGET":
        state.budget = message
        state.current_step = "PEOPLE"
    elif current_step == "PEOPLE":
        state.people = message
        state.current_step = "COMPLETED"
        # Generate itinerary
        itinerary = ai_service.generate_itinerary(
            state.source, state.destination, state.days, 
            state.vibe, state.budget, state.people
        )
        state.itinerary = itinerary
    
    db.commit()
    db.refresh(state)
    
    if state.current_step == "COMPLETED":
        return f"{STEPS['COMPLETED']}\n\n{state.itinerary}"
    
    return STEPS[state.current_step]
