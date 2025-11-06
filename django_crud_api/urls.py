from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

# ViewSets
from barbers.views import BarberViewSet
from servicios.views import ServicioViewSet
from proveedores.views import ProveedorViewSet

# FBVs de reservas
from reservas.views import (
    crear_reserva,
    listar_reservas,
    obtener_reserva,
    confirmar_reserva,
    rechazar_reserva,
    horarios_disponibles,
    # 👇 nuevos endpoints para el panel del cliente
    listar_reservas_cliente,
    reservas_cliente_contadores,
)

# ✅ Router único para todos los ViewSets
router = DefaultRouter()
router.register(r'barbers', BarberViewSet, basename='barbers')
router.register(r'servicios', ServicioViewSet, basename='servicios')
router.register(r'proveedores', ProveedorViewSet, basename='proveedores')

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ API base (incluye todos los ViewSets)
    path('api/', include(router.urls)),

    # ----- USUARIOS -----
    path('api/usuarios/', include('usuarios.urls')),

    # ----- RESERVAS (FBV) -----
    path('api/reservas/crear/', crear_reserva, name='reservas-crear'),
    path('api/reservas/', listar_reservas, name='reservas-listar'),
    path('api/reservas/<int:reserva_id>/', obtener_reserva, name='reservas-obtener'),
    path('api/reservas/<int:reserva_id>/confirmar/', confirmar_reserva, name='reservas-confirmar'),
    path('api/reservas/<int:reserva_id>/rechazar/', rechazar_reserva, name='reservas-rechazar'),

    # 👇 NUEVOS: cliente
    path('api/reservas/cliente/', listar_reservas_cliente, name='reservas-cliente'),
    path('api/reservas/cliente/contadores/', reservas_cliente_contadores, name='reservas-cliente-contadores'),

    # ----- HORARIOS DISPONIBLES (MÚLTIPLES ALIAS) -----
    path('api/horarios/', horarios_disponibles, name='horarios'),
    path('api/reservas/horarios/', horarios_disponibles, name='reservas-horarios'),
    path('api/horarios-disponibles/', horarios_disponibles, name='horarios-disponibles'),
]

# Servir archivos MEDIA en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
