package main

import (
	"fmt"
	"sort"
)

func MergeSorted(a, b []int) []int {
	c := make([]int, 0, len(a)+len(b))
	var idxA, idxB int
	for idxA < len(a) && idxB < len(b) {
		if a[idxA] < b[idxB] {
			c = append(c, a[idxA])
			idxA++
		} else {
			c = append(c, b[idxB])
			idxB++
		}
	}
	if idxA < len(a) {
		c = append(c, a[idxA:]...)
	}

	if idxB < len(b) {
		c = append(c, b[idxB:]...)
	}

	return c
}

func MergeSortedReslice(a, b []int) []int {
	c := make([]int, 0, len(a)+len(b))
	for len(a) > 0 && len(b) > 0 {
		if a[0] < b[0] {
			c = append(c, a[0])
			a = a[1:]
		} else {
			c = append(c, b[0])
			b = b[1:]
		}
	}
	c = append(c, a...)
	c = append(c, b...)

	return c
}

func MergeBySort(a, b []int) []int {
	c := make([]int, 0, len(a)+len(b))
	c = append(c, a...)
	c = append(c, b...)
	sort.Ints(c)
	return c
}

func main() {
	a := []int{1, 2, 4}
	b := []int{4, 6, 10}
	fmt.Println(MergeSorted(a, b))
	fmt.Println(MergeBySort(a, b))
}
