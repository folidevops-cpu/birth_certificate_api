import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models import database_models

def test_database():
    db = SessionLocal()
    try:
        # Test basic certificate query
        certificates = db.query(database_models.Certificate).all()
        print(f"\nTotal certificates in database: {len(certificates)}")
        
        if len(certificates) > 0:
            cert = certificates[0]
            print(f"\nSample certificate details:")
            print(f"Registration number: {cert.registration_number}")
            print(f"Title: {cert.title}")
            
            # Test child relationship
            if cert.child:
                print(f"\nChild details:")
                print(f"Name: {cert.child.name}")
                print(f"Sex: {cert.child.sex}")
            else:
                print("\nNo child record found")
            
            # Test father relationship
            if cert.father:
                print(f"\nFather details:")
                print(f"Name: {cert.father.name}")
                print(f"Nationality: {cert.father.nationality}")
            else:
                print("\nNo father record found")
            
            # Test mother relationship
            if cert.mother:
                print(f"\nMother details:")
                print(f"Name: {cert.mother.name}")
                print(f"Nationality: {cert.mother.nationality}")
            else:
                print("\nNo mother record found")
        else:
            print("No certificates found in database")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    test_database()