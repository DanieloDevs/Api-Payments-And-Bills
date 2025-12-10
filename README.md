# 📌 Sistema de Gestión de Gastos y Pagos (Django REST + MySQL)

## 🧾 Descripción del Proyecto

Este proyecto implementa un **sistema de control de gastos y pagos** para una empresa, diseñado para gestionar el ciclo completo de aprobación y procesamiento de pagos.

### Funcionalidades principales:

- Registrar gastos (Bills)
- Aprobar o cancelar gastos
- Generar pagos asociados
- Validar saldo bancario antes de procesar pagos
- Registrar histórico completo de transacciones
- API REST completa construida con Django REST Framework

**Objetivo:** Demostrar diseño de software profesional, arquitectura limpia, modelado de datos robusto y mejores prácticas con Django REST Framework.

---

## 🧩 Diagrama ER (MER)

El modelo entidad-relación define las entidades principales del sistema:

- **Bank_Account** → Cuentas bancarias donde se descuenta el dinero
- **Bills** → Representan los gastos registrados
- **Payments** → Ejecución del pago de un gasto
- **Transaction_History** → Registro de todos los cargos y pagos

### Relaciones principales:

- Un `Bill` puede generar un `Payment`
- Un `Payment` pertenece a una `Bank_Account`
- Toda acción queda registrada en `Transaction_History`

### 📎 MER completo:

> **TODO:** Agregar el diagrama del modelo entidad-relación

![MER](URL_AQUI)

---

## 🔄 Diagrama de Flujo del Proceso

Representa el ciclo completo del sistema:

1. Creación del gasto
2. Aprobación
3. Generación del pago
4. Validación de saldo
5. Ejecución y finalización

### 📎 Diagrama de flujo:

> **TODO:** Agregar el diagrama de flujo del proceso

![Diagrama de Flujo](URL_AQUI)

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión |
|-----------|---------|
| Python | 3.x |
| Django | Latest |
| Django REST Framework | Latest |
| MySQL | 8.0+ |
| Postman | Para pruebas de API |

---

## 📂 Estructura del Proyecto
```
proyecto-gastos/
│
├── core/
│   ├── models.py          # Modelos de datos
│   ├── serializers.py     # Serializadores DRF
│   ├── views.py           # Lógica de vistas/endpoints
│   └── urls.py            # Rutas de la API
│
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🧱 Modelos Principales

### BankAccount

- `name` - Nombre de la cuenta
- `account_number` - Número de cuenta
- `bank` - Banco asociado
- `balance` - Saldo disponible

### Bill

- `description` - Descripción del gasto
- `amount` - Monto
- `status` - Estado: `pending`, `approved`, `cancelled`, `paid`

### Payment

- `bill_id` - Referencia al gasto
- `account_id` - Cuenta bancaria asociada
- `amount` - Monto a pagar
- `status` - Estado del pago
- Fechas: `creation`, `approval`, `cancellation`, `payment`

### TransactionHistory

- `account_id` - Cuenta involucrada
- `payment_id` - Pago relacionado
- `amount` - Monto de la transacción
- `type` - Tipo: `charge` o `payment`

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/proyecto-gastos.git
cd proyecto-gastos
```

### 2️⃣ Crear entorno virtual
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar base de datos MySQL

Edita el archivo `settings.py` y configura la conexión a MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'expenses_db',
        'USER': 'root',
        'PASSWORD': 'TU_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Iniciar el servidor
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

---

## 🧪 Uso y Pruebas con Postman

### Crear un gasto (Bill)

**Endpoint:** `POST /api/bills/`

**Body (JSON):**
```json
{
  "description": "Compra de insumos",
  "amount": 1500.50
}
```

### Aprobar un gasto

**Endpoint:** `POST /api/bills/1/approve/`

### Crear un pago vinculado

**Endpoint:** `POST /api/payments/`

### Aprobar un pago

**Endpoint:** `POST /api/payments/1/approve/`

### Ejecutar pago y descontar del banco

**Endpoint:** `POST /api/payments/1/pay/`

---

## 🧠 Lógica de Negocio

### Flujo completo del proceso:

1. Se crea un gasto en estado `pending`
2. El gasto se aprueba → cambia a `approved`
3. Se genera un pago asociado al gasto
4. El pago se aprueba y se valida el saldo disponible
5. Si hay saldo suficiente → se descuenta y el pago se marca como `paid`
6. Toda la operación se registra en el historial de transacciones

---

## 📺 Puntos Clave para Entrevistas

Este proyecto demuestra:

- ✅ **Modelado de datos profesional** - Diseño de base de datos normalizado y escalable
- ✅ **Manejo de estados y flujos complejos** - Gestión de estados de gastos y pagos
- ✅ **Diseño de API REST** - Endpoints bien estructurados siguiendo mejores prácticas
- ✅ **Clean Code** - Código mantenible y documentado
- ✅ **Seguridad y consistencia** - Validaciones en cada transición de estado
- ✅ **Documentación clara** - README completo y fácil de seguir

---

## 📄 Licencia

Este proyecto está bajo licencia MIT.

---

## 👤 Autor

**Brandon Daniel Ortiz Mejia**

- GitHub: https://github.com/DanieloDevs
- LinkedIn: https://www.linkedin.com/in/danielodev/

