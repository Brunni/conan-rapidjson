#include "rapidjson/document.h"
#include <iostream>

using namespace rapidjson;

int main(){
	const char json[] = "[1, 2, 3, 4]";
	StringStream s(json);
	Document d;
	d.ParseStream(s);
	std::cerr << "Successful test of rapidjson";
	return 0;
}
