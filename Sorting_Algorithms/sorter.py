# Bubble Sort Class
class BubbleSorter:

    def sort(self, data):
        pointer = len(data) - 1
        while pointer > 0:
            for i in range(pointer):
                if data[i] > data[i + 1]:
                    temp = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = temp
            pointer -= 1
        return data


# Insertion Sort Class
class InsertionSorter:

    def sort(self, data):
        for i in range(len(data) - 1):
            j = i

            while data[j + 1] < data[j] and j > -1:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                j -= 1
        return data


# Selection Sort Class
class SelectionSorter:

    def sort(self, data):
        pointer = 0
        temp_pointer = 0
        while pointer < len(data) - 1:
            smallest = data[pointer]
            for i in range(pointer + 1, len(data)):
                if smallest > data[i]:
                    smallest = data[i]
                    temp_pointer = i
            if pointer != len(data):
                temp = data[pointer]
                data[pointer] = smallest
                data[temp_pointer] = temp
                pointer += 1
        return data

#BucketSortClass
class BucketSort:

    def sort(self, input_list):
        # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket
        max_value = max(input_list)
        size = max_value / len(input_list)

        # Create n empty buckets where n is equal to the length of the input list
        buckets_list = []
        for x in range(len(input_list)):
            buckets_list.append([])

            # Put list elements into different buckets based on the size
        for i in range(len(input_list)):
            j = int(input_list[i] / size)
            if j != len(input_list):
                buckets_list[j].append(input_list[i])
            else:
                buckets_list[len(input_list) - 1].append(input_list[i])

        # Sort elements within the buckets using Insertion Sort
        for z in range(len(input_list)):
            BucketSort.insertion_sort(self, buckets_list[z])

        # Concatenate buckets with sorted elements into a single list
        final_output = []
        for x in range(len(input_list)):
            final_output = final_output + buckets_list[x]
        return final_output

    def insertion_sort(self, bucket):
        for i in range(1, len(bucket)):
            var = bucket[i]
            j = i - 1
            while (j >= 0 and var < bucket[j]):
                bucket[j + 1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var