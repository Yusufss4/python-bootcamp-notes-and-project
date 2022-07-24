# Project Aim

Learning Object-Oriented in Python Programming - Example Project

A simple interface using the Object-Oriented side of the Python Programming that is capable of creating a class, adding students to these classes, adding grades to these students and in the end calculating the grades according to the method that you specified and exporting these results to excels. 

# Why?

To learn the Object-Oriented in Python Programming by coding a simple project. 

# How to Run and Build?

1. Run the interface script. 
2. Continue according to the introductions specified in the menu.

# To Do

- Currently there is no control if anything goes wrong, this means that for example if a student doesnt exists that you want to add grade for it is going to give an exception an crash.

# Notes

### Why we use __name__ == '__main__': ?

__name__ is a speacial variable that is called when we run the program or the module itself is imported. 

When the __name__ is run from the main module and you run that module __name__ equals __main__, otherwise it is equal to the module name. 

Here is the **first_module**. When you run it directly the __name__ will be main and it is going to call the main() method.

```python
print("This will always run be either imported or run directly.")
print(f"First Module's Name: {__name__}")

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    main()
```

Here is the **second module.** To call the main method we have to use class_name.main() otherwise it will not  be called when imported. 

```python
import first_module

first_module.main()

print(f"Second Module's Name: {__name__}")
```

 __name__ == '__main__' is helping us to decide which code will be run or not when imported. 

Here is a video about it: 

[https://www.youtube.com/watch?v=sugvnHA7ElY](https://www.youtube.com/watch?v=sugvnHA7ElY)