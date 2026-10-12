package main

import (
	"crypto/sha256"
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "<h1>Go</h1><p>net/http</p>")
	})
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) { fmt.Fprint(w, "ok") })
	http.HandleFunc("/cpu", func(w http.ResponseWriter, r *http.Request) {
		h := sha256.Sum256([]byte("seed"))
		for i := 0; i < 20000; i++ {
			h = sha256.Sum256(h[:])
		}
		fmt.Fprintf(w, "%x", h[:4])
	})
	http.ListenAndServe(":3000", nil)
}
