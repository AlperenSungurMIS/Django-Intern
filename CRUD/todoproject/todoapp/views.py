from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Bir Todo oluşturma (Create View)
def createTodoView(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")  # Başarılı oluşturma sonrası yönlendirme
    template_name = "todoapp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)

# Tüm Todo'ları listeleme (List View)
def showTodoView(request):
    obj = Todo.objects.all()  # Tüm Todo verilerini alır
    template_name = "todoapp/show.html"
    context = {"obj": obj}
    return render(request, template_name, context)

# Bir Todo'yu güncelleme (Update View)
def updateTodoView(request, f_id):
    obj = Todo.objects.get(id=f_id)  # Güncellenecek Todo'yu id ile bul
    form = TodoForm(instance=obj)  # Mevcut Todo verileriyle formu başlat
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)  # Verilerle formu güncelle
        if form.is_valid():
            form.save()  # Güncellenen veriyi kaydet
            return redirect("show_url")  # Güncelleme sonrası yönlendirme
    template_name = "todoapp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)

# Bir Todo'yu silme (Delete View)
def deleteTodoView(request, f_id):
    obj = Todo.objects.get(id=f_id)  # Silinecek Todo'yu bul
    if request.method == "POST":
        obj.delete()  # Silme işlemini gerçekleştir
        return redirect("show_url")  # Silme sonrası yönlendirme
    template_name = "todoapp/confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)
