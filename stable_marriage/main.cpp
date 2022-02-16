#include <iostream>
#include <vector>
using namespace std;
vector<int> getStableMarriage(vector<vector<int>> B, vector<vector<int>> G, int _m, int _w)
{
    pair<int, bool> tmp(-1, false);
    vector<pair<int, bool>> men(_m, tmp); // first: the last request,second: is engaged or not
    vector<int> women(_w, -1);
    bool flag = true;
    while (flag)
    {
        flag = false;
        for (int i = 0; i < _m; i++)
        {
            if (men[i].second == false) // he's free
            {
                if (men[i].first == -1)
                {
                    for (int j = 0; j < _w; j++)
                        if (B[i][j] == 1)
                        {
                            men[i].first = j;
                            break;
                        }
                }
                else
                {
                    for (int j = 0; j < _w; j++)
                        if (B[i][j] == B[i][men[i].first] + 1)
                        {
                            men[i].first = j;
                            break;
                        }
                }

                if (women[men[i].first] == -1)
                {
                    women[men[i].first] = i;
                    men[i].second = true;
                }
                else
                {
                    flag = true;
                    if (G[men[i].first][i] < G[men[i].first][women[men[i].first]])
                    {
                        int rejected = women[men[i].first];
                        men[rejected].second = false;
                        women[men[i].first] = i;
                        men[i].second = true;
                    }
                }
            }
        }
    }
    return women;
}
void print(vector<int> res, int code)
{
    if (code == 1)
        cout << "girl"
             << "      "
             << "boy\n";
    else
        cout << "boy"
             << "      "
             << "girl\n";
    for (int i = 0; i < res.size(); i++)
        cout << i + 1 << "          " << res[i] + 1 << endl;
}
int main()
{
    int m; // number of men
    int w; // number of women

    cout << "number of men:\n";
    cin >> m;
    cout << "number of women:\n";
    cin >> w;
    cout << "preference matrix:\n";
    vector<int> tmp(w, 0);
    vector<vector<int>> Bprefer(m, tmp);
    vector<int> tmp2(m, 0);
    vector<vector<int>> Gprefer(w, tmp);

    for (int i = 0; i < m; i++)
        for (int j = 0; j < w; j++)
            cin >> Bprefer[i][j] >> Gprefer[j][i];

    vector<int> res;
    cout << "Boy optimal:\n";
    res = getStableMarriage(Bprefer, Gprefer, m, w);
    print(res, 1);

    cout << "Girl optimal:\n";
    res = getStableMarriage(Gprefer, Bprefer, w, m);
    print(res, 2);

    return 0;
}