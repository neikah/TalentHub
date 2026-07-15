from role_required import group_required
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

@group_required("HR Manager", "Employee", "Admin")
def document_list(request):
    documents = Document.objects.all().order_by('-uploaded_at')

    return render(
        request,
        'documents/document_list.html',
        {
            'documents': documents
        }
    )

@group_required("HR Manager", "Employee", "Admin")
def upload_document(request):

    if request.method == "POST":

        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('document_list')

    else:

        form = DocumentForm()

    return render(
        request,
        'documents/upload_document.html',
        {
            'form': form
        }
    )