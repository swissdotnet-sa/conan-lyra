#include "lyra/lyra.hpp"

int main()
{
    int width = 0;
    auto cli = cli_parser()
        | lyra::opt( width, "width" )
            ["-w"]["--width"]
            ("How wide should it be?");
}
