from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('bookshef.can_create', raise_exception=True)
def create_book():
    return

@permission_required('bookshef.can_edit', raise_exception=True)
def edit_book():
    return

@permission_required('bookshef.can_view', raise_exception=True)
def view_book():
    return

@permission_required('bookshef.can_delete', raise_exception=True)
def delete_book():
    return