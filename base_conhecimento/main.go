package main

import "fmt"

func main() {
	var lista = []int{10, 20, 30}

	for i := 0; i < len(lista); i++ {
		fmt.Println(lista[i])
	}

	for _, n := range lista {
		fmt.Println(n)
	}
}
