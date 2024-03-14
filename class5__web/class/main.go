package main

import (
	"fmt"
	"net/http"
)

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("New user occured")
		w.Write([]byte("Hello user!"))
	})

	http.ListenAndServe(":8080", mux)
}
