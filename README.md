📌 – Sistema de Gestión de Gastos y Pagos (Django REST + MySQL)

🧾 Descripción del Proyecto

Este proyecto implementa un sistema de control de gastos y pagos para una empresa.
Permite:

Registrar gastos (Bills)

Aprobar o cancelar gastos

Generar pagos asociados

Validar saldo bancario antes de pagar

Registrar histórico de transacciones

Consumir todo mediante una API REST construida con Django

El objetivo es demostrar diseño de software, arquitectura limpia, modelado de datos profesional y uso de Django REST Framework.


🧩 Diagrama ER (MER)

El modelo entidad-relación define las entidades principales:

Bank_Account → cuentas donde se descuenta el dinero

Bills → representan gastos

Payments → ejecución del pago de un gasto

Transaction_History → registro de cargos y pagos

✔ Relación principal

Un Bill puede generar un Payment

Un Payment pertenece a una Bank_Account

Toda acción queda registrada en Transaction_History

📎 MER completo (imagen):
👉 TODO: pegar aquí el link de tu imagen del MER
![MER](URL_AQUI)

🔄 Diagrama de Flujo del Proceso

Representa todo el ciclo: creación del gasto, aprobación, generación del pago, validación de saldo y finalización.

📎 Diagrama de flujo:
👉 TODO: pegar aquí el link de tu diagrama de flujo
![Diagrama de Flujo](URL_AQUI)

🛠️ Tecnologías Utilizadas

Python 3.x

Django

Django REST Framework

MySQL

Postman (para pruebas)

📂 Estructura Principal
core/
 ├── models.py
 ├── serializers.py
 ├── views.py
 └── urls.py

🧱 Modelos Principales (Resumen)
BankAccount

name

account_number

bank

balance

Bill

description

amount

status (pending, approved, cancelled, paid)

Payment

bill_id

account_id

amount

status

fechas: creation, approval, cancellation, payment

TransactionHistory

account_id

payment_id

amount

type (charge / payment)

🚀 Instalación y Configuración
1️⃣ Clonar el repositorio


git clone https://github.com/usuario/proyecto-gastos.git
cd proyecto-gastos
2️⃣ Crear entorno virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Instalar dependencias
pip install -r requirements.txt
4️⃣ Configurar base de datos MySQL

Agrega en settings.py:

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

5️⃣ Migraciones


python manage.py makemigrations
python manage.py migrate
6️⃣ Ejecutar el servidor

python manage.py runserver

🧪 Uso y Pruebas en Postman
✔ Crear un gasto (Bill)

POST
/api/bills/

Body JSON:

{
  "description": "Compra de insumos",
  "amount": 1500.50
}

✔ Aprobar un gasto

POST
/api/bills/1/approve/

✔ Crear un pago vinculado

POST
/api/payments/

✔ Aprobar un pago

POST
/api/payments/1/approve/

✔ Pagar y descontar del banco

POST
/api/payments/1/pay/

🧠 Lógica del Negocio (Resumen)

Se crea un gasto en estado pending.

Si el gasto se aprueba → cambia a approved.

Opcionalmente se genera un pago asociado.

El pago se aprueba y luego se valida si la cuenta tiene saldo.

Si tiene saldo → se descuenta y se marca paid.

Se registra todo en el historial de transacciones.

📺 Explicación para Entrevistas

Este proyecto muestra:

Dominio de modelado de datos

Manejo de estados y flujos complejos

Buen diseño de API y clean code

Seguridad y consistencia en cada transición

Documentación clara y mantenible
