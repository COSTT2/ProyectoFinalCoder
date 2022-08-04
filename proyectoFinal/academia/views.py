from ast import Return
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from academia.models import Curso, profesores
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView

def inicio(request):
    return render(request, "academia/inicio.html")

# --- views profesores ---

class listaProfesores(ListView):
    model = profesores
    template_name = "academia/lista_profesores.html"
    
class crearProfesores(CreateView):
    model = profesores
    template_name = "academia/form_profesores.html"
    success_url = "/academia/profesores/lista"
    fields = ["nombre", "apellido", "especialidad", "mail", "educacion", "imagen"]
    
class mostrarProfesores(DetailView):
    model = profesores
    template_name = "academia/informacion_profesores.html"

class editarProfesores(UpdateView):
    model = profesores
    template_name = "academia/form_profesores.html"
    success_url = "/academia/profesores/lista"
    fields = ["nombre", "apellido", "especialidad", "mail", "educacion", "imagen"]

class borrarProfesores(DeleteView):
    model = profesores
    template_name = "academia/borrar_profesores.html"
    success_url = "/academia/profesores/lista"
    
# --- views cursos ---
    
class cursosLista(ListView):
    model = Curso
    template_name = "academia/lista_cursos.html"

class mostrarCurso(DetailView):
    model = Curso
    template_name = "academia/informacion_cursos.html"
    
class editarCurso(UpdateView):
    model = Curso
    template_name = "academia/form_cursos.html"
    success_url = "/academia/cursos/lista"
    fields = ["titulo", "descripcion", "contenido", "imagen", "duracion"]
    
class borrarCurso(DeleteView):
    model = Curso
    template_name = "academia/borrar_cursos.html"
    success_url = "/academia/cursos/lista"

class crearCursos(CreateView):
    model = Curso
    template_name = "academia/form_cursos.html"
    success_url = "/academia/cursos/lista"
    fields = ["titulo", "descripcion", "contenido", "imagen", "duracion"]
    
# --- views usuarios ---
    
class edicionUsuario(LoginRequiredMixin, UpdateView):
    model = User
    template_name ="perfil_usuario/usuario_form.html"
    fields = ["email", "primer_nombre", "apellido"]
    
    def get_success_url(self):
        return reverse_lazy("informacionUsuario", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs["pk"])
    
class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'academia/crear_cuenta_form.html'
  success_url = reverse_lazy('login')
  form_class = UserCreationForm
  success_message = "Se creo tu perfil satisfactoriamente"
    
def peticion_login(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                
                return render(request, "academia/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )
            
            else:
                
                return render(request, "academia/inicio.html", {"mensaje":f"Error, los son datos incorrectos"} )
            
        else: 
            
                return render(request, "academia/inicio.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    
    return render(request,"academia/login.html", {"form":form} )

