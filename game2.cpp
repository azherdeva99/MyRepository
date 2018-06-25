
#include <vector>
#include <iostream>
#include <iomanip>
#include <conio.h>
#include <cstdlib>

using std::vector;
using std::cout;

const unsigned short SIZE = 4; // the size of the playing field

vector<int> in_game_area(SIZE);
vector<vector<int>> game_area(SIZE, in_game_area); //game card

vector<int> in_right_area(SIZE);
vector<vector<int>> right_area(SIZE, in_right_area); // the right card

struct coordinate // coordinates of the zero element
{
    unsigned x;
    unsigned y;
} zero;

void create_right_area() // create the right playing field
{
    unsigned right_value = 1;
    for (unsigned i = 0; i < SIZE; i++)
    {
        for (unsigned j = 0; j < SIZE; j++)
            right_area[i][j] = right_value++;
    }
    right_area[SIZE-1][SIZE-1] = 0; // zero element in the lower right corner
}

void create_game_area() // random playing field
{
    unsigned limit = SIZE*SIZE;
    vector<int> temporary;
    for (unsigned i = 0; i < limit; i++)
        temporary.push_back(i);

    int value;
    for (unsigned i = 0; i < SIZE; i++)
    {
        for (unsigned j = 0; j < SIZE; j++)
        {
            value = rand() % limit--;
            game_area[i][j] = temporary[value];
            if (temporary[value] == 0) // keep the coordinates of the zero element
            {
                zero.x = j;
                zero.y = i;
            }
            temporary.erase(temporary.begin() + value);
        }
    }
}

bool check_area()
{
    if (game_area == right_area)
        return true;
    return false;
}

void up_move() //move down
{
    if (zero.y < SIZE - 1)
    {
        game_area[zero.y][zero.x] = game_area[zero.y + 1][zero.x];
        zero.y++;
        game_area[zero.y][zero.x] = 0;
    }
}

void down_move() //move up
{
    if (zero.y > 0)
    {
        game_area[zero.y][zero.x] = game_area[zero.y - 1][zero.x];
        zero.y--;
        game_area[zero.y][zero.x] = 0;
    }
}

void right_move() // move to the left
{
    if (zero.x > 0)
    {
        game_area[zero.y][zero.x] = game_area[zero.y][zero.x - 1];
        zero.x--;
        game_area[zero.y][zero.x] = 0;
    }
}

void left_move() // move to the right
{
    if (zero.x < SIZE - 1)
    {
        game_area[zero.y][zero.x] = game_area[zero.y][zero.x + 1];
        zero.x++;
        game_area[zero.y][zero.x] = 0;
    }
}

void get_direction() // determination of the pressed arrow
{
    int move = static_cast<int> (_getch()); // UP = 72, DOWN = 80, RIGHT = 77, LEFT = 75
    switch (move)
    {
        case 72:
        {
            up_move(); break;
        }
        case 80:
        {
            down_move(); break;
        }
        case 77:
        {
            right_move(); break;
        }
        case 75:
        {
            left_move(); break;
        }
        default:
        {
            get_direction();
        }
    }
}
void screen() // output to the screen
{
    system("cls");
    for (unsigned i = 0; i < SIZE; i++)
    {
        for (unsigned j = 0; j < SIZE; j++)
        {
            if (game_area[i][j] != 0)
                cout << std::setw(2) << std::setfill('0') << game_area[i][j] << ' ';
            else
                cout << "** "; // zero element
        }
        cout << '\n';
    }
}

int main()
{
    srand(static_cast<int>(time(NULL)));

    create_right_area(); // creating game maps
    do
    {
        create_game_area();
    } while (check_area());

    do // the game loop
    {
        screen();
        get_direction();
    }
    while (!check_area());

    cout << "\nCongratulations!\nGame over!\n";
    _getch();
}
