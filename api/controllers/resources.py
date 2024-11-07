from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

# Functions for handling resources
def create_resource(db: Session, resource):
    # Create a new instance of the Resource model with the provided data
    db_resource = models.Resource(
        customer_name=resource.customer_name,
        description=resource.description
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def read_all_resources(db: Session):
    return db.query(models.Resource).all()


def read_one_resource(db: Session, resource_id):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()


def update_resource(db: Session, resource_id, resource):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    update_data = resource.model_dump(exclude_unset=True)
    db_resource.update(update_data, synchronize_session=False)
    db.commit()
    return db_resource.first()


def delete_resource(db: Session, resource_id):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_resource.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
