public class Counter {
    private int value;

    public Counter(int initialValue) {
        this.value = initialValue;
    }

    public int getValue() {
        return value;
    }

    public void increment() {
        value++;
    }
}
