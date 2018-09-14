#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Prato {
    int id;
    int custo;
    float lucro;
    float custo_beneficio;
};

bool pode_cozinhar(const Prato &prato, int orcamento) {
    return prato.custo <= orcamento;
}

vector<Prato> solucionar(const vector<Prato> &pratos,
                         int dias, int orcamento) {
    vector<Prato> menu;
    int ultimo = -1;

    int j, k;
    j = k = 0;
    for (int i = 0; i < dias; i++) {
        Prato p = pratos[j];

        while (j < pratos.size() && !pode_cozinhar(p, orcamento)) {
            j++;
            k++;
            
            if (j < pratos.size()) {
                p = pratos[j];
            }
        }

        if (j >= pratos.size()) {
            break;
        }

        menu.push_back(p);
        orcamento -= p.custo;

        if (ultimo != -1 && p.id != pratos[ultimo].id) {
            j = k;
        } else {
            ultimo = j;
            j++;
        }       
    }

    if (j >= pratos.size()) {
        menu = {};
    }
    
    return menu;
}

int main() {
    int dias, num_pratos, orcamento;
    cin >> dias >> num_pratos >> orcamento;

    while (dias != 0 || num_pratos != 0 || orcamento != 0) {
        vector<Prato> aux1;
        vector<Prato> aux2;

        for (int i = 0; i < num_pratos; i++) {
            int custo;
            float lucro;
            cin >> custo >> lucro;
            aux1.push_back({i + 1, custo, lucro, custo/lucro});
            aux1.push_back({i + 1, custo, lucro/2, custo/(lucro/2)});
            aux2.push_back({i + 1, custo, 0, 0});
        }

        sort(aux1.begin(), aux1.end(),
             [](const Prato &p1, const Prato &p2)
             { return p1.custo_beneficio < p2.custo_beneficio ||
                     (p1.custo_beneficio == p2.custo_beneficio
                      && p1.custo < p2.custo); });
        
        sort(aux2.begin(), aux2.end(),
             [](const Prato &p1, const Prato &p2)
             { return p1.custo < p2.custo; });

        vector<Prato> pratos;
        pratos.insert(pratos.begin(), aux1.begin(), aux1.end());
        pratos.insert(pratos.end(), aux2.begin(), aux2.end());

        float lucro_total = 0;
        vector<Prato> menu = solucionar(pratos, dias, orcamento);
        for (auto &p : menu) {
            lucro_total += p.lucro;
        }

        printf("%.1f\n", lucro_total);
        if (lucro_total > 0) {
            for (auto &p : menu) {
                cout << p.id << " ";
            }
            cout << endl;
        }
        cout << endl;
            
        cin >> dias >> num_pratos >> orcamento;
    }
    
    return 0;
}
