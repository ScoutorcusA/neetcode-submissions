class DynamicArray {

    int[] initial_array;
    int capacity;
    int first_free_index;

    public DynamicArray(int capacity) 
    {
        this.capacity = capacity;
        initial_array = new int [capacity];
        first_free_index = 0; // This variable will keep track of the first open space in the
                              // array

    }

    public int get(int i) 
    {
        return initial_array[i];

    }

    public void set(int i, int n) 
    { 
        initial_array[i] = n;

    }

    public void pushback(int n) 
    {
        if(first_free_index > capacity-1)
        {
            resize();
        }
        initial_array[first_free_index] = n;
        first_free_index++;
        

    }

    public int popback() {
        first_free_index--;
        return initial_array[first_free_index];

    }

    private void resize() 
    {
        int[] temp = new int[capacity*2];
        capacity *= 2;
        for(int i = 0; i<first_free_index;i++)
        {
            temp[i] = initial_array[i];
        }

        initial_array = temp;

    }

    public int getSize() {
        return first_free_index;

    }

    public int getCapacity() {
        return capacity;

    }
}
