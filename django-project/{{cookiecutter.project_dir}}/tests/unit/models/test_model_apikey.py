import pytest
from django.db import IntegrityError

from {{cookiecutter.package_name}}.models import ApiKey


@pytest.mark.django_db(transaction=True)
def test_unique_case_insensitivity(user, group):
    ApiKey.objects.create(name="aaa", user=user, role=group)
    with pytest.raises(IntegrityError, match='violates unique constraint "unique_key_name_for_user"'):
        ApiKey.objects.create(name="AAA", user=user, role=group)
    assert ApiKey.objects.create(name="ABC", user=user, role=group)
