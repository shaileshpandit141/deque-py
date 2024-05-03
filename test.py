from deque import Deque


def main() -> None:
    # Create a new deque
    deque: Deque  = Deque()

    # Insert elements
    deque.insert_front(10)
    deque.insert_front(0)

    # Insert elements
    deque.insert_rear(20)
    deque.insert_rear(30)

    # Output deque status
    print("Deque element: ", deque)
    print("Size of Deque: ", len(deque))
    print("Font element: ", deque.get_font())
    print("Rear element: ", deque.get_rear())

    # Delete elements
    deque.delete_front()
    deque.delete_rear()

    # Output deque status
    print("Deque element: ", deque)
    print("Size of Deque: ", len(deque))
    print("Font element: ", deque.get_font())
    print("Rear element: ", deque.get_rear())


if __name__ == "__main__":
    main()
