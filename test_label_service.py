import pytest
from app.api.models import LabelIn, LabelOut

labels = LabelIn(
    name='Dead Dynasty',
    phone='+7999999999',
    count_artists=5,
    county='Russia',
)


def test_create_label(labels: LabelIn = labels):
    assert dict(labels) == {'name': labels.name,
                            'phone': labels.phone,
                            'city': labels.city,
                            'country': labels.country
                            }


def test_update_label_city(labels: LabelIn = labels):
    labels_upd = LabelIn(
        name='Dead Dynasty',
        phone='+7999999999',
        count_artists=5,
        county='Russia',
        id=1
    )
    assert dict(labels_upd) == {'name': labels.name,
                                'phone': labels.phone,
                                'city': labels.city,
                                'country': labels.country,
                                'id': labels_upd.id}


def test_update_label_city(labels: LabelIn = labels):
    labels_upd = LabelIn(
        name='Dead Dynasty',
        phone='+7999999999',
        count_artists=5,
        county='Russia',
        id=1
    )
    assert dict(labels_upd) == {'name': labels.name,
                                'phone': labels.phone,
                                'city': labels.city,
                                'country': labels.country,
                                'id': labels_upd.id
                                }