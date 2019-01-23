from typing import NamedTuple


class Entity(NamedTuple):
    value: str
    label: str


class EntityConstants:
    VIEW_ARRIVALS = Entity(value='view_arrivals', label='View Arrivals')

    VIEW_SALES_REPORT = Entity(value='view_sales_report', label='View Sales Report')


EntityConstants.ENTITY_CHOICES = [
    (entity.value, entity.label)
    for item_constant, entity in vars(EntityConstants).items()
    if isinstance(entity, Entity)
]
