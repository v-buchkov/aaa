package main

import (
	"math/rand"
	"sort"
	"testing"
)

const size = 1000000

func generateRandomSortedArray(size int) []int {
	arr := make([]int, 0, size)
	for i := 0; i < size; i++ {
		arr = append(arr, rand.Intn(size))
	}
	sort.Ints(arr)
	return arr
}

func BenchmarkMerge(b *testing.B) {
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		a := generateRandomSortedArray(size)
		bb := generateRandomSortedArray(size)
		b.StartTimer()
		MergeSorted(a, bb)
	}
}

func BenchmarkMergeBySort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		a := generateRandomSortedArray(size)
		bb := generateRandomSortedArray(size)
		b.StartTimer()
		MergeBySort(a, bb)
	}
}
