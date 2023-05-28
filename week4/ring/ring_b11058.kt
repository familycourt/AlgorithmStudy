val kriii = mutableListOf<Long>(0, 1, 2, 3, 4, 5, 6)

fun main() {
    val input: Long = readln().toLong()
    for (i in 7..input) {
        kriii.add(getMax(i.toInt()))
    }
    print(kriii[input.toInt()])
}

fun getMax(num: Int): Long {
    val tmp = mutableListOf<Long>()

    for (i in 3 until num) {
        tmp.add(kriii[num- i] * (i-1))
    }
    return tmp.max()
}