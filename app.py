from glob import escape
from bs4 import BeautifulSoup
import requests
import os
import datetime

# funcion para limpiar la consola, usa la librearia "os"
def clear():
    os.system("cls||clear");

clear()
# consigo los valores de compra y venta del mercado del dolar en el dia de la fecha
site = "https://dolarhoy.com/";
try:
    resultado = requests.get(site);
except:
    print("Error al conectar a la pagina, verifique el estado de su conexion a internet o el estado de la pagina: https://dolarhoy.com")
    input("-Enter para salir-")
content = resultado.text;

soup = BeautifulSoup(content, "html.parser");

# dentro del html de la pagina de dolarhoy, si te fijas con el F12, los valores de compra y venta se encuentran en un <div> y estos divs tienen la clase "val"
box = soup.find_all("div", class_="val");

# como en la pagina de dolarhoy hay varios valores de compra y venta (dolar oficial promedio, dolar bolsa, liqui, etc) solo agarro los dos primeros valores
# del array que me devuelve la instruccion de arriba, porque justo estos coninciden con ser el del dolar blue
valorCompra = box[0].get_text();
valorVenta = box[1].get_text();

# a los valores compra venta se les saca el simbolo de "$" del string para que puedan ser casteados a float correctamente
valorPromedio = (float(valorCompra.replace("$","")) + float(valorVenta.replace("$",""))) / 2;



def pasarPesoADolar(pesos):
    resultado = (pesos / valorPromedio);
    # round redondea en este caso al 3 decimal
    print(round(resultado, 3));

def pasarDolarAPeso(dolares):
    resultado = (dolares * valorPromedio);
    # round redondea en este caso al 3 decimal
    print(round(resultado, 3));

def printMenu(fecha):
    print(f"Programa de cambio de moneda (peso, dolar)       -|Precios ({fecha.day}/{fecha.month}/{fecha.year})|-  Compra: " + valorCompra + "   Venta: " + valorVenta);
    print("\nIngrese 1 para cambiar pesos(ARS) a dolares");
    print("Ingrese 2 para cambiar dolares a pesos(ARS)       nota: el precio de dolar utilizado es un promedio del de compra y venta");
    print("\n'exit' para salir");


# dependiendo de la opcion del input del usuario intenta castear el input a float, y pasarselo como argumento a la funcion
# si no puede castearlo correctamente printea "input error"
def inputOption(option):
    if option == "1":
        print("\nIngrese el monto en pesos");
        pesos = input("-> ");
        try:
            pasarPesoADolar(float(pesos));
        except ValueError:
            print("input error");
        input("Enter para continuar");

    elif option == "2":
        print("\nIngrese el monto en dolares");
        dolares = input("-> ");
        try:
            pasarDolarAPeso(float(dolares));
        except ValueError:
            print("input error");
        input("Enter para continuar");

# funcion main, funciona hasta que el usuario mande "exit"
def main():
    while(True):
        fecha = datetime.datetime.now();
        clear();
        printMenu(fecha);
        option = input("\n-> ");
        if option == "exit":
            break;
        else:
            inputOption(option);

main();