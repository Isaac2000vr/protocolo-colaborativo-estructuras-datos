fun main() {
    val numeros = IntArray(10) { (1..100).random() }

    println("Arreglo generado")
    println(numeros.joinToString(", "))

    println("\nRecorrido con for clásico:")
    for (i in 0 until numeros.size) {
        println("Posición $i: ${numeros[i]}")
    }

    println("\nRecorrido con for-each:")
    for (numero in numeros) {
        println(numero)
    }

    val sinImpares = numeros.copyOf()
    for (i in sinImpares.indices) {
        if (sinImpares[i] % 2 != 0) {
            sinImpares[i] = 0
        }
    }

    println("\nValores impares cambiados por cero:")
    println(sinImpares.joinToString(", "))

    val multiplicados = numeros.copyOf()
    for (i in multiplicados.indices) {
        multiplicados[i] = multiplicados[i] * i
    }

    println("\nValores multiplicados por su índice:")
    println(multiplicados.joinToString(", "))


    val valorBuscado = numeros[3]
    val posicion = busquedaLineal(numeros, valorBuscado)

    if (posicion != -1) {
        println("\nEl valor $valorBuscado se encontró en la posición $posicion")
    } else {
        println("\nEl valor $valorBuscado no se encontró en el arreglo")
    }

    val valorInexistente = 999
    val posicion2 = busquedaLineal(numeros, valorInexistente)

    if (posicion2 != -1) {
        println("El valor $valorInexistente se encontró en la posición $posicion2")
    } else {
        println("El valor $valorInexistente no se encontró en el arreglo")
    }
}

fun busquedaLineal(arreglo: IntArray, valorBuscado: Int): Int {
    for (i in arreglo.indices) {
        if (arreglo[i] == valorBuscado) {
            return i
        }
    }
    return -1
}