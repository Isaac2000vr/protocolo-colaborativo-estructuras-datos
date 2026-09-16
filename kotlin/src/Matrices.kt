fun main() {
    val matriz = Array(3) { IntArray(3) }
    var contador = 1

    for (fila in 0 until 3) {
        for (columna in 0 until 3) {
            matriz[fila][columna] = contador
            contador++
        }
    }

    println("Matriz en forma de tabla:")
    for (fila in matriz) {
        for (valor in fila) {
            print("$valor ")
        }
        println()
    }

    println("\nRecorrido por columnas:")
    for (columna in 0 until 3) {
        for (fila in 0 until 3) {
            print("${matriz[fila][columna]} ")
        }
        println()
    }

    var suma = 0
    for (fila in matriz) {
        for (valor in fila) {
            suma += valor
        }
    }

    println("\nSuma de todos los elementos: $suma")

    val temp = matriz[0]
    matriz[0] = matriz[2]
    matriz[2] = temp

    println("\nMatriz con primera y última fila intercambiadas:")
    for (fila in matriz) {
        for (valor in fila) {
            print("$valor ")
        }
        println()
    }
}