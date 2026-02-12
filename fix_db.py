from backend.app.database import engine
from backend.app import models

def fix_db():
    print("Updating database schema...")
    try:
        # This will create missing tables, but won't add columns to existing ones
        models.Base.metadata.create_all(bind=engine)
        
        # Manually add the itinerary column if it doesn't exist (SQLite)
        with engine.connect() as conn:
            try:
                # Use text() to avoid SQLAlchemy warning about raw SQL strings
                from sqlalchemy import text
                conn.execute(text("ALTER TABLE trip_planner_state ADD COLUMN itinerary TEXT"))
                # conn.commit() # Not always needed depending on engine config, but safe
                print("Added 'itinerary' column to 'trip_planner_state'")
            except Exception as e:
                if "duplicate column name" in str(e).lower():
                    print("Column 'itinerary' already exists.")
                else:
                    print(f"Note: {e}")
        
        print("Database schema update complete.")
    except Exception as e:
        print(f"Error updating database: {e}")

if __name__ == "__main__":
    fix_db()
