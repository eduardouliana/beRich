package main

import (
	"fmt"

	"berich.com/lets/go/entity"
	"berich.com/lets/go/utils"
)

func main() {
	fmt.Println("Let's Be Rich")

	var draws []entity.Draw

	all_sorted_draws := utils.ReadFile("allDraws.json")

	for key, value := range all_sorted_draws {
		var draw = &entity.Draw{
			ID:      key,
			Numbers: value,
		}

		draws = append(draws, *draw)
	}

	// Paridade
	for i := 0; i < len(draws); i++ {
		Odd := 0
		PairNumbers := 0

		for num := range draws[i].Numbers {
			if num%2 == 0 {
				Odd++
			} else {
				PairNumbers++
			}
		}
		draws[i].OddNumbers = Odd
		draws[i].PairNumbers = PairNumbers
	}

	for i := 0; i < len(draws); i++ {
		fmt.Printf("%s - %d", draws[i].ID, draws[i].Numbers)
		fmt.Printf("Pares: %d - Ímpares: %d", draws[i].PairNumbers, draws[i].OddNumbers)
		fmt.Println()
	}

	utils.SaveToFile("teste.json", draws)
}
