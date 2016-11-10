#include <iostream>

template < typename type >

class CircularBuffer
{
private:
    type * arr;             // массив-буфер
    int bufferSize;        // размер буфера
    int length;            // кол-во элементов в буффере
    int head;              // индекс первого элемента
    int tail;              // индекс последнего элемента

public:

    CircularBuffer( int size )
    {
        head = tail = length = 0;
        bufferSize = size;
        arr = new type[bufferSize];
    }

    ~CircularBuffer()
    {
        delete[] arr;
    }

    //перегрузка оператора индексации
    int& operator [] (int i) { return arr[i]; }

    // Добавить элемент
    void put( const int & value )
    {
        if ( tail == bufferSize )
        {
            tail = 0;
        }

        arr[tail] = value;
        ++tail;
        ++length;
    }


    // Извлечь последний элемент
    int & pop()
    {
        if ( head == bufferSize ) {
            head = 0;
        }
        int & elem = arr[head];
        ++head;
        --length;
        return elem;
    }

    // Кол-во элементов в буфере
    size_t size() const
    {
        return length;
    }

    // Ёмкость буфера
    size_t capacity() const
    {
        return bufferSize;
    }

    // Напечатать в одну строчку значения переменных head, tail и содержимое буфера
    void printBuffer()
    {
        std::cout << head << ' ' << tail << ' ';
        for (int i = 0; i < size(); i++){
            std::cout << arr[i] << ' ';
        }
        std::cout << std::endl;
    }
};


int main()
{
    CircularBuffer<int> buf(3);

    for( int i = 0; i < 11; ++i )
    {
        buf.put( i * 2 );
        buf.printBuffer();
        if ( buf.size() == buf.capacity() ) {
            std::cout << "---------------" << std::endl;
            while( buf.size() ) {
                std::cout << buf.pop() << std::endl;
            }
        }

    }

    std::cout << "---------------" << std::endl;
    while( buf.size() ) {
        std::cout << buf.pop() << std::endl;
    }
    std::cout << "---------------" << std::endl << "проверка перегрузки оператора индексации: " << buf[0] << ' ' << buf[1];
    return 0;
}