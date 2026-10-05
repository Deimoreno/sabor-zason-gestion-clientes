import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


from gestion_clientes import GestionClientes

#====================#
#  VENTANA PRINCIPAL #
#====================#  

ventana = tk.Tk()

ventana.title("Sabor & Zason - Gestion Clientes")
ventana.geometry("500x350")
ventana.resizable(False,False)

# Color personalizado 
ventana.configure(bg="#94F1E5")

#=======================#
#     LOGO Y TITULO     #
#=======================#

logo = tk.Label(
    ventana,
    text="🍲🍱",
    font=("Times New Roman", 35),
    bg="#FBDAA4"
)
logo.pack(pady=15)

titulo = tk.Label(
    ventana,
    text="SABOR & ZASON",
    font=("Arial", 22, "bold"),
    bg="#F4E6D7"
)

titulo.pack()


autor = tk.Label(
    ventana,
    text="Desarrollado por: Deiber Mena Moreno",
    font=("Arial", 12, "italic"),
    bg="#F4E6D7"
)
autor.pack(pady=10)

            #=================================#
            #          CONTRASEÑA             #
            #=================================#

etiqueta = tk.Label(
    ventana,
    text="Ingrese la contraseña:",
    font=("Arial", 11),
    bg="#F4E6D7"
)
etiqueta.pack(pady=5)

entrada_password = tk.Entry(
    ventana,
    show="*",
    width=25,
)

entrada_password.pack(pady=10)

#====================================#
#  FUNCION PARA VERIFICAR CONTRASEÑA #
#====================================#

def verificar_password():
    password = entrada_password.get()
    if password == "1793" :
        abrir_registro()
        
    else:
        messagebox.showerror(
            "error",
            "Contraseña incorrecta"
        )

    #======================#
    #    BOTON INGRESAR    #
    #======================#

boton_ingresar = tk.Button(
    ventana,
    text="INGRESAR",
    width=20,
    command=verificar_password,

)

boton_ingresar.pack(pady=20)

#============================================#
#  FUNCION PARA ABRIR EL FORMULARIO REGISTRO #
#============================================#

def abrir_registro():
    ventana_registro = tk.Toplevel(ventana)

    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    ventana_registro.title("Registro de Clientes")
    ventana_registro.geometry("600x700")


    # Variable para almacenar el cliente guardado
    cliente_guardado = None

    #============================#
    #            TITULO          #
    #============================# 

    titulo = tk.Label(
        ventana_registro,
        text="🍽️ REGISTRO DE CLIENTES  🍽️",
        font=("Arial", 22, "bold"),
    )

    titulo.pack(pady=22)

#=====================#
#   IDENTIFICACION    #
#=====================#

    tk.Label(
        ventana_registro,
        text="Identificacion:",
    ).pack()

    entrada_identificacion = tk.Entry(
        ventana_registro,
        width=40
    )
    entrada_identificacion.pack(pady=5)

# NOMBRE

    tk.Label(
        ventana_registro,
        text="Nombre Completo:"
    ).pack()

    entrada_nombre = tk.Entry(
        ventana_registro,
        width=40
    )

    entrada_nombre.pack(pady=5)

    tk.Label(
        ventana_registro,
        text="Genero:"
    ).pack()

# GENERO

    combo_genero = ttk.Combobox(
        ventana_registro,
        values=["Masculino", "Femenino",],
        state="readonly",
        width=37
    )

    combo_genero.pack(pady=5)

# MENÚ

    tk.Label(
        ventana_registro,
        text="Tipo de Menú:"
    ).pack()

# MENÚ COMBOBOX

    combo_menu = ttk.Combobox(
        ventana_registro,
        values=[
            "Ejecutivo",
            "Vegetariano",
            "Degustación",
            "Infantil",
            "Gourmet",
        ],
        state="readonly",
        width=37
        
    )

    combo_menu.pack(pady=5)

# Numero de sesiones 

    tk.Label(
        ventana_registro,
        text="Número de Sesiones:"
    ).pack()

    entrada_sesiones = tk.Entry(
        ventana_registro,
        width=40
    )
    entrada_sesiones.pack(pady=5)

# FECHA DE REGISTRO

    tk.Label(
        ventana_registro,
        text="Fecha de Registro:"
    ).pack()

    etiqueta_fecha = tk.Label(
    ventana_registro,
    text=fecha_actual
    )
    etiqueta_fecha.pack(pady=5)

# COSTO POR SESIÓN

    tk.Label(
        ventana_registro,
        text="Costo por sesión:"
        ).pack()

    entrada_costo = tk.Entry(
        ventana_registro,
        width=40,
        state="disabled"
    )
    entrada_costo.pack(pady=5)

#===========================================================#
# FUNCION PARA ACTUALIZAR COSTOS SEGUN EL MENÚ SELECCIONADO #
#===========================================================#

    def actualizar_costos(event):
        precios = {
        "Ejecutivo": 35000,
        "Vegetariano": 28000,
        "Degustación": 75000,
        "Infantil": 20000,
        "Gourmet": 95000
    }

        costo = precios.get(combo_menu.get(), 0)

        entrada_costo.config(state="normal")
        entrada_costo.delete(0, tk.END)
        entrada_costo.insert(0, str(costo))
        entrada_costo.config(state="disabled")

    combo_menu.bind("<<ComboboxSelected>>", actualizar_costos)

#==================#
# GUARDAR REGISTRO #
#==================#

    def guardar_registro():

        identificacion = entrada_identificacion.get()
        nombre = entrada_nombre.get()
        genero = combo_genero.get()
        menu = combo_menu.get()

#VALIDACION DE IDENTIFICACION

        if identificacion == "":
            messagebox.showerror(
                "Error",
                "Ingrese la identificación."
            )
            return

        #VALIDACION DE NOMBRE

        if nombre == "":
            messagebox.showerror(
                "Error",
                "Ingrese el nombre completo."
            )
            return

        #VALIDACION DE GÉNERO

        if genero == "":
            messagebox.showerror(
                "Error",
                "Seleccione el género."
            )
            return

        #VALIDACION DE MENÚ

        if menu == "":
            messagebox.showerror(
                "Error",
                "Seleccione el tipo de menú."
            )
            return

        
        #Validación de número de sesiones

        try:
            sesiones = int(entrada_sesiones.get())

        except ValueError:
            messagebox.showerror(
                "Error",
                "El número de sesiones debe ser en número entero."
            )
            return
        

        if sesiones <= 0:
            messagebox.showerror(
                "Error",
                "El número de sesiones debe ser mayor a cero."
            )
            return
        
        fecha = etiqueta_fecha.cget("text")
        costo = float(entrada_costo.get())

        cliente = GestionClientes(
            identificacion,
            nombre,
            genero,
            menu,
            sesiones,
            fecha,
            costo
    )

        total = cliente.calcularCostoTotal()

        messagebox.showinfo(
            "Registro guardado",
            f"Cliente: {cliente.nombreCompleto}\n"
            f"Menú: {cliente.tipoMenu}\n"
            f"Sesiones: {cliente.numeroSesiones}\n"
            f"Costo total: ${total:,.0f}"
        )

        mostrar_reporte(cliente, total )

        entrada_identificacion.delete(0, tk.END)
        entrada_nombre.delete(0, tk.END)
        combo_genero.set("")
        combo_menu.set("")
        entrada_sesiones.delete(0, tk.END)

        entrada_costo.config(state="normal")
        entrada_costo.delete(0, tk.END)
        entrada_costo.config(state="disabled")


    #==================================#
    # CALCULAR COSTO Y MOSTRAR REPORTE #
    #==================================#

    def mostrar_reporte(cliente,total):
        ventana_reporte = tk.Toplevel(ventana_registro)

        ventana_reporte.title("Reporte del cliente")
        ventana_reporte.geometry("500x500")

        titulo_reporte = tk.Label(
            ventana_reporte,
            text="REPORTE DEL CLIENTE",
            font=("Arial", 22, "bold"),

        )

        titulo_reporte.pack(pady=20)

        tk.Label(
            ventana_reporte,
            text=f"Identificación: {cliente.identificacion}"
        ).pack(pady=5)

        tk.Label(
            ventana_reporte,
            text=f"Nombre: {cliente.nombreCompleto}"
        ).pack(pady=5)

        tk.Label(
            ventana_reporte,
            text=f"Genero: {cliente.genero}"
        ).pack(padx=5)

        tk.Label(
            ventana_reporte,
            text=f"Tipo de menú: {cliente.tipoMenu}"
        ).pack(pady=5)

        tk.Label(
            ventana_reporte,
            text=f"Número de sesiones: {cliente.numeroSesiones}"
        ).pack(pady=5)

        tk.Label(
            ventana_reporte,
            text=f"Fecha de registro: {cliente.fechaRegistro}"
        ).pack(pady=5)

        tk.Label(
            ventana_reporte,
            text=f"Costo por sesión: $ {cliente.costoPorSesion:,.0f}"
        ).pack(pady=5)

        tk.Label(
            ventana_reporte,
            text=f"COSTO TOTAL: ${total:,.0f}",
            font=("Arial", 14, "bold")
        ).pack(pady=20)


    #========================#
    # SALIR DE LA APLICACION #
    #========================#

    def salir_aplicacion():

        respuesta = messagebox.askyesno(
            "Salir" ,
            "¿Esta seguro de que desea salir de la aplicación?"
        )

        if respuesta:
            ventana.destroy()

    #=============================#
    # BOTON PARA GUARDAR REGISTRO #
    #=============================#

    boton_guardar = tk.Button(
        ventana_registro,
        text="GUARDAR REGISTRO",
        width=25,
        command=guardar_registro
    )

    boton_guardar.pack(pady=8)



    boton_salir = tk.Button(
        ventana_registro,
        text="SALIR DE LA APLICACION",
        width=25,
        command=salir_aplicacion
    )
    boton_salir.pack(pady=8)


boton_ingresar.pack(pady=20)   

ventana.mainloop()