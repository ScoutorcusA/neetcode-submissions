class DynamicArray {
    private  int[] temp ;
    private int element_current = 0;
    private int capacity;

    public DynamicArray(int capacity) {
        temp = new int [capacity];
        this.capacity = capacity;


    }

    public int get(int i) {
        return temp[i];

    }

    public void set(int i, int n) {

        temp[i] = n;

    }

    public void pushback(int n) {

        if (capacity <= element_current)
        {
            this.resize();
        }

        this.set(element_current, n);
        element_current +=1;


    }

    public int popback() {
        
        element_current -= 1;

        return temp[element_current];

    }

    private void resize() {
        int[] new_array = new int [capacity* 2];
        for(int i = 0; i < temp.length; i++)
        {
            new_array[i] = temp[i];

            
        }

        temp = new_array;
        capacity = capacity * 2;


    }

    public int getSize() {
        return element_current;

    }

    public int getCapacity() {
        return capacity;

    }
}
