#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int* ptr; // initialize a pointer
    int foo = 23; // arbitrary var
    int bar = 69; // arbitrary var
    ptr = &foo; // pointer refers to the address of foo
    int& ref = bar; // a reference to bar
    cout << "address of ptr: " << ptr << endl;
    cout << "value of ptr: " << *ptr << endl;
    cout << "reference ref: " << ref << endl;
    cout << "reference ref: " << &ref << endl;

    return 0;
}