#include<bits/stdc++.h>
using namespace std;

struct node{
    int deadline;
    int profit;
};

bool acompare(node a,node b){
    if(a.profit > b.profit)
        return true;
    else if(a.profit == b.profit)
        return a.deadline < b.deadline;
    else
        return false;
}

int main()
{
    int n;
    int totalProfit = 0;
    cin >> n;

    node nodes[n];
    int i,dmax=0;
    for (i=0;i<n;++i){
        cin >> nodes[i].deadline;
        if(dmax <= nodes[i].deadline)
            dmax = nodes[i].deadline;
    }
    for (i=0;i<n;++i){
        cin >> nodes[i].profit;
    }

    sort(nodes,nodes+n,acompare);
    cout << "\nSorted nodes : \n";
    for(i=0;i<n;++i){
        cout << nodes[i].deadline << "  ";
    }
    cout << endl;
    for(i=0;i<n;++i){
        cout << nodes[i].profit << " ";
    }

    int jobs[dmax];
    for(i=0;i<dmax;++i){
        jobs[i] = 0;
    }
    for(i=0;i<n;++i){
        int j;
        j = nodes[i].deadline;
        while(j>0){
            if(jobs[j-1] == 0){
                jobs[j-1] = nodes[i].profit;
                totalProfit += nodes[i].profit;
                break;
            }
            --j;
        }
    }

    cout << endl << endl << "Ans:\n";
    for(i=0;i<dmax;++i){
        cout << jobs[i] << " ";
    }
    cout << endl;
    cout << "Total Profit = " << totalProfit << endl;
    return 0;
}
