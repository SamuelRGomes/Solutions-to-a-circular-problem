class MaxBinaryHeap {
  constructor() {
    this.values = [];
  }
  insert(element) {
    this.values.push(element);
    this.bubbleUp(element);
    console.log(this.values);
  }
  bubbleUp(element) {
    let insertIdx = this.values.length - 1;
    while (insertIdx > 0) {
      let parentIdx = Math.floor((insertIdx - 1) / 2);
      let parent = this.values[parentIdx];
      if (element > parent) {
        this.values[parentIdx] = element;
        this.values[insertIdx] = parent;
        insertIdx = parentIdx;
      } else {
        break;
      }
    }
  }
  ExtractMax() {
    const max = this.values[0];
    const end = this.values.pop();
    if (this.values.length > 0) {
      this.values[0] = end;
      this.bubbleDown();
    }
    return max;
  }
  bubbleDown() {
    let idx = 0;

    const element = this.values[0];
    while (true) {
      let leftChildIdx = 2 * idx + 1;
      let rightChildIdx = 2 * idx + 2;
      let swapIdx = null;
      if (leftChildIdx <= this.values.length - 1) {
        let leftChild = this.values[leftChildIdx];
        if (leftChild > element) {
          swapIdx = leftChildIdx;
        }
      }
      if (rightChildIdx <= this.values.length - 1) {
        let rightChild = this.values[rightChildIdx];
        if (
          (swapIdx === null && rightChild > element) ||
          (swapIdx !== null && rightChild > leftChild)
        ) {
          swapIdx = rightChildIdx;
        }
      }
      if (swapIdx === null) break;
      this.values[idx] = this.values[swapIdx];
      this.values[swapIdx] = element;
      idx = swapIdx;
    }
  }
}

let heap = new MaxBinaryHeap();
heap.insert(41);
heap.insert(39);
heap.insert(33);
heap.insert(18);
heap.insert(27);
heap.insert(12);
heap.insert(55);
