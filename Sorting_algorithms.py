class sorting_algorithms():
    def bubble_sort(self, arr):   
        for i in range(len(arr) - 1):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]           
        return arr
    
    def merge_sort(self, arr):
        no_of_elements = len(arr)
        if no_of_elements == 1:
            return arr
  
        middle_element = no_of_elements // 2

        left_partition = self.merge_sort(arr[:middle_element])
        right_partition = self.merge_sort(arr[middle_element:])

        return self.merge(left_partition, right_partition)

    def merge(self, left, right):
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr
    
    def heapify(self, arr, n, i):
        largest_value = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[largest_value] < arr[left]:
            largest_value = left
        if right < n and arr[largest_value] < arr[right]:
            largest_value = right
        if largest_value != i:
            arr[i], arr[largest_value] = arr[largest_value], arr[i]
            self.heapify(arr, n, largest_value)

    def heap_sort(self, arr):
        no_of_elements = len(arr)
        for i in range(no_of_elements // 2 - 1, -1, -1):
            self.heapify(arr, no_of_elements, i)
        for i in range(no_of_elements - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr

    def quick_sort_regular(self, arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1
        def quicksort(arr, left, right):
            if left >= right:
                return
            pivot = self.partition(arr, left, right)
            quicksort(arr, left, pivot - 1)
            quicksort(arr, pivot + 1, right)
        return quicksort(arr, left, right)

    def partition(self, arr, left, right):
        pivot_position = left
        for i in range(left + 1, right + 1):
            if arr[i] <= arr[left]:
                pivot_position += 1
                arr[i], arr[pivot_position] = arr[pivot_position], arr[i]
        arr[pivot_position], arr[left] = arr[left], arr[pivot_position]
        return pivot_position

    def quick_sort_median(self, arr):
        def quickSortMedian(left, right):
            if(left >= right):
                return
            medians = ( int )( ( left + right ) / 2 )
            if( 
                ( 
                    ( arr[left] <= arr[medians] ) and ( arr[medians] <= arr[right] ) )
                    or ( ( arr[right] <= arr[medians] ) and ( arr[medians] <= arr[left] ) 
                    ) 
                ):
                pass
            elif(
                ( 
                    ( arr[medians] <= arr[left] ) and ( arr[left] <= arr[right] ) )
                    or ( ( arr[right] <= arr[left] ) and ( arr[left] <= arr[medians] ) 
                    )
                ):
                arr[left], arr[medians] = arr[medians], arr[left]      
            elif(
                ( 
                    ( arr[left] <= arr[right] ) and ( arr[right] <= arr[medians] ) ) 
                    or ( ( arr[medians] <= arr[right] ) and ( arr[right] <= arr[left] ) 
                    ) 
                ):
                arr[right], arr[medians] = arr[medians], arr[right]     

            pivot = arr[ medians ]
            arr[ medians ] = arr[ right ]

            i = left
            j = right - 1
            while( i <= j ):
                while( i < right and arr[i] <= pivot ):
                    i += 1
                while( j >= left and arr[j] >= pivot ):
                    j -= 1

                if( i < j ):
                    arr[ i ], arr[ j ] = arr[ j ], arr[ i ]                    
                    i += 1
                    j -= 1

            arr[ right ] = arr[ j + 1 ]
            arr[ j + 1 ] = pivot

            quickSortMedian(left, j)
            quickSortMedian(j + 2, right)
            return arr
    
        quickSortMedian(0, len(arr)-1)
        return arr
    
    def selection_sort(self, arr):   
        for i in range(len(arr)):        
            idx = i        
            for j in range(i+1, len(arr)):            
                if arr[j] < arr[idx]:
                    idx = j        
            arr[i], arr[idx] = arr[idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        for i in range(len(arr),):
            curr_value = arr[i]
            curr_position = i
            while curr_position > 0 and arr[curr_position - 1] >curr_value:
                arr[curr_position] = arr[curr_position - 1]
                curr_position = curr_position - 1    
            arr[curr_position] = curr_value
        return arr
