#include <iostream>
#include <string>
#include <algorithm>
#include <ctime>
using namespace std;

// function to convert the string in lowercase
string toLowerCase(const string &str)
{
    string result = str;
    transform(result.begin(), result.end(), result.begin(), ::tolower);
    return result;
}
// function to get the current time as a string
string getCurrentTime()
{
    time_t now = time(0);
    tm *ltm = localtime(&now);
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%I:%M %p", ltm);
    return string(buffer);
}

// function to get the current day as a string
string getCurrentDay()
{
    time_t now = time(0);
    tm *ltm = localtime(&now);

    char buffer[80];
    strftime(buffer, sizeof(buffer), "%A", ltm);

    return string(buffer);
}
// function to get the chatbot response based on a user input
string chatbotResponse(const string &userInput)
{
    string input = toLowerCase(userInput);
    // greeting
    if (input.find("hello") != string::npos || input.find("hi") != string::npos)
    {
        return "hello how can i help you today";
    }
    else if (input.find("bye") != string::npos || input.find("goodbye") != string::npos)
    {
        cout<<"have a sweat dreams";
        return "Goodbye! Have a great day!";
    }
    // Asking for time
    else if (input.find("time") != string::npos)
    {
        return "The current time is " + getCurrentTime();
    }
    // Asking for day
    else if (input.find("day") != string::npos)
    {
        return "Today is " + getCurrentDay();
    }
    // Unknown input
    else
    {
        return "I'm sorry, I don't understand that.";
    }
}
int main()
{
    cout << "Chatbot: Hello! How can I assist you today?" << endl;
    string userInput;
    while (getline(cin, userInput))
    {
        string response = chatbotResponse(userInput);
        cout << "Chatbot: " << response << endl;
        if (userInput == "bye" || userInput == "goodbye")
            break;
    }
    return 0;
}