#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

template<int metre, int kilogram, int second, int Ampere, int kelvin, int mole, int candela>
class DimQ
{
private:
    double value;
    map<string, int> Dimension = {{'m', metre},
                                  {'kg', kilogram},
                                  {'s', second},
                                  {'A', Ampere},
                                  {'K', kelvin},
                                  {'mol', mole},
                                  {'cd', candela}};

public:

    DimQ(double v) {
        value = v;
    }

    double getValue(){
        return value;
    }

    DimQ operator-() {
        return DimQ(-value);
    }


    DimQ operator+(const DimQ &other) const {
        return DimQ(value + other.value);
    }

    DimQ operator-(const DimQ &other) const {
        return DimQ(value - other.value);
    }

    template<int m, int kg, int s, int A, int K, int mol, int cd>
    DimQ<metre + m, kilogram + kg, second + s, Ampere + A, kelvin + K, mole + mol, candela + cd>
    operator*(DimQ<m, kg, s, A, K, mol, cd>& other) {
        return DimQ<metre + m, kilogram + kg, second + s, Ampere + A, kelvin + K, mole + mol, candela + cd>(
                value * other.getValue());
    }

    template<int m, int kg, int s, int A, int K, int mol, int cd>
    DimQ<metre - m, kilogram - kg, second - s, Ampere - A, kelvin - K, mole - mol, candela - cd>
    operator/(DimQ<m, kg, s, A, K, mol, cd>& other) {
        return DimQ<metre - m, kilogram - kg, second - s, Ampere - A, kelvin - K, mole - mol, candela - cd>(
                value / other.getValue());
    }

    friend ostream &operator<<(ostream &out, const DimQ &D) {
        out << D.value;
        map<string, int>::iterator i;
        for (i = D.Dimension.begin(); i != D.Dimension.end(); ++i){
            if (i->second != 0){
                out << i->first << '^' << i->second;
            }
        }
        return out;
    }

};


int main() {
    typedef DimQ<1, 0, 0, 0, 0, 0, 0> Length;
    typedef DimQ<0, 1, 0, 0, 0, 0, 0> Mass;
    typedef DimQ<0, 0, 1, 0, 0, 0, 0> Time;
    typedef DimQ<0, 0, 0, 1, 0, 0, 0> Amperage;
    typedef DimQ<0, 0, 0, 0, 1, 0, 0> Temperature;
    typedef DimQ<0, 0, 0, 0, 0, 1, 0> Amount;
    typedef DimQ<0, 0, 0, 0, 0, 0, 1> Intensity;
    typedef DimQ<1, 0, -1, 0, 0, 0, 0> Speed;
    typedef DimQ<1, 0, -2, 0, 0, 0, 0> Acceleration;
    typedef DimQ<0, 0, 0, 0, 0, 0, 0> Constant;
    DimQ<1, 0, 0, 0, 0, 0, 0> S1(10);
    Length S2(13);
    Mass M1(1);
    std::cout << "Проверка перегрузки оператора унарного минуса: " << -S1 << std::endl;
    std::cout << "Проверка перегрузки оператора бинароного сдвига: " << S1 << std::endl;
    std::cout << "Проверка перегрузки оператора бинарного плюса: " << S1 + S2 << std::endl;
    std::cout << "Проверка перегрузки оператора бинарного минуса: " << S1 - S2 << std::endl;
    std::cout << S1*S2 << " "<< S1*M1;
    //std::cout << M1 + S1 << std::endl; //Так делать нельзя
    return 0;
}