object Solution {
  def solution(lottos: Vector[Int], win_nums: Vector[Int]): Vector[Int] = {
    var aMatch: Int = 0
    var zeros: Int = 0

    for (lotto <- lottos) {
      if (lotto == 0) {
        zeros += 1
      }
    }

    for (win_num <- win_nums) {
      aMatch += lottos.count(lotto => { lotto == win_num })
    }

    val minRank: Int = if (7 - (aMatch + zeros) < 7) 7 - (aMatch + zeros) else 6
    val maxRank: Int = if (7 - aMatch < 7) 7 - aMatch else 6

    return Vector[Int](minRank, maxRank)
  }

  def main(args: Array[String]): Unit = {
    val lottos: Vector[Int] = Vector(44, 1, 0, 0, 31, 25)
    val win_nums: Vector[Int] = Vector(31, 10, 45, 1, 6, 19)

    println(solution(lottos, win_nums))
  }
}
