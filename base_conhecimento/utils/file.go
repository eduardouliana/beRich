package utils

import (
	"encoding/json"
	"io/ioutil"
	"log"

	"berich.com/lets/go/entity"
)

func ReadFile(fileName string) map[string][]int {
	var data map[string][]int

	file, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Fatal(err)
	}

	err = json.Unmarshal(file, &data)
	if err != nil {
		log.Fatal(err)
	}

	return data
}

func SaveToFile(fileName string, data []entity.Draw) {
	file, _ := json.MarshalIndent(data, "", " ")

	ioutil.WriteFile(fileName, file, 0644)
}
