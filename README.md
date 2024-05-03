# Deque Python Module

The Deque Python module provides an implementation of the Deque (double-ended queue) data structure. A deque is a versatile data structure that allows efficient insertion and deletion at both ends, making it suitable for various applications where items need to be added or removed from the front or rear of a collection.

## Features

### 1. Insertion and Deletion
  * `insert_front(data):` Insert an element at the front of the deque.
  * `insert_rear(data):` Insert an element at the rear of the deque.
  * `delete_front():` Delete an element from the front of the deque.
  * `delete_rear():` Delete an element from the rear of the deque.

### 2. Get Front and Rear Elements
  * `is_empty():` Check if the deque is empty.
  * `size():` Get the current size of the deque.

## Installation
1. Clone Deque repository using git
   ```bash
   git clone kasdfjkafkdf
   ```
2. Then, You can install the deque module via pip:
   ```bash
   pip install .
   ```

## Usage
```py
from deque import Deque

# Create a new deque
deque = Deque()

# Insert elements
deque.insert_front(10)
deque.insert_front(0)
deque.insert_rear(20)
deque.insert_rear(30)

# Output deque status
print("Deque element:", deque)
print("Size of Deque:", len(deque))
print("Front element:", deque.get_front())
print("Rear element:", deque.get_rear())

# Delete elements
deque.delete_front()
deque.delete_rear()

# Output deque status after deletion
print("Deque element:", deque)
print("Size of Deque:", len(deque))
print("Front element:", deque.get_front())
print("Rear element:", deque.get_rear())
```

## Testing
To ensure the correctness of the Deque module, a test script (test.py) is provided. You can run the test script using the following command:
```bash
python test.py
```

## License
This project is licensed under the terms of the MIT license. See the LICENSE.txt file for details.

## Author
If you have any questions or need assistance with this project, please contact Shailesh at shaileshpandit141@gmail.com.

Thank you for using `Deque` module.


