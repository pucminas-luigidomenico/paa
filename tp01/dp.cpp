#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;
    
int main() {
    // Dias, pratos e orçamento
    int k, n, m;
    cin >> k >> n >> m;

    while (k != 0 || n != 0 || m != 0) {
        vector<int> custos(n);
        vector<int> lucros(n);

        for (int i = 0; i < n; i++) {
            cin >> custos[i] >> lucros[i];
        }

        // Matriz para programacao dinamica:
        // [0..k-1 dias][0..n - 1 pratos][0..m orcamento]
        // Inicializa todas as posicoes com -1
        // O -1 vai servir para indicar situacoes em que o prato
        // nao pode ser cozinhado, devido ao orcamento
        vector<vector<vector<float>>> dp(k, vector<vector<float>>(n, vector<float>(m + 1, -1)));

        // Matriz para guardar o "caminho" feito pelo prato,
        // guardando o prato anterior que gerou aquele lucro
        // [0..k-1 dias][o..n - 1 pratos][0..m orcamento]
        // -1: nenhum prato cozinhado anteriormente
        vector<vector<vector<short>>> caminho(k, vector<vector<short>>(n, vector<short>(m + 1, -1)));

        for (int dia = 0; dia < k; dia++) {
            for (int prato = 0; prato < n; prato++) {
                for (int orc = 1; orc < m + 1; orc++) {
                    // Se nao for possivel cozinhar, passa para
                    // proxima iteracao
                    if (orc - custos[prato] < 0) {
                        continue;
                    }

                    // Se for o primeiro dia, nao ha dias
                    // anteriores para acumular lucro
                    if (dia == 0) {
                        dp[dia][prato][orc] = lucros[prato];

                        // Senao, eh preciso comparar com dias
                        // anteriores e pegar o maior lucro
                    } else {
                        float lucro_max = -1;
                        int prato_ant = -1;
                        
                        // Percorrer todos os pratos do dia anterior,
                        // testando se eh uma combinacao possivel e
                        // atualizando o maior lucro
                        for (int p = 0; p < n; p++) {
                            // Se lucro do prato no dia anterior
                            // for -1, significa que nao foi possivel
                            // cozinha-lo e, portanto, nao eh uma combinacao
                            // possivel para o prato atual.
                            if (dp[dia - 1][p][orc - custos[prato]] == -1) {
                                continue;
                            }

                            float lucro_parcial = dp[dia - 1][p][orc - custos[prato]];
                            // Se for uma combinacao possivel, eh preciso
                            // testar se eh o mesmo prato e se eh uma
                            // repeticao acontecendo pela segunda ou
                            // mais vezes
                            if (p == prato) {
                                // Se for 1 repeticao, o lucro do prato
                                // cai pela metade. Se for duas, o lucro
                                // do prato cai para zero e, portanto, o
                                // lucro parcial eh apenas o lucro anterior
                                if (caminho[dia - 1][p][orc - custos[prato]] != prato) {
                                    lucro_parcial += lucros[prato] / 2.0;
                                }

                                // Senao, o prato nao esta sendo repetido e o lucro
                                // deve ser integral
                            } else {
                                lucro_parcial += lucros[prato];
                            }

                            // Se o lucro parcial for maior que o lucro anterior,
                            // atualizar lucro maximo e prato anterior
                            if (lucro_parcial > lucro_max) {
                                lucro_max = lucro_parcial;
                                prato_ant = p;

                                // Senao,s e o lucro parcial for igual ao anterior,
                                // dar prioridade primeiro ao prato que nao esteja
                                // sendo repetido e, caso nao exista essa situacao, ao
                                // prato com menor custo.
                            } else if (lucro_parcial == lucro_max) {
                                if (p != prato) {
                                    if (prato_ant == prato) {
                                        prato_ant = p;
                                    } else if (custos[p] < custos[prato_ant]) {
                                        prato_ant = p;
                                    }
                                }
                            }
                        }
                        dp[dia][prato][orc] = lucro_max;
                        caminho[dia][prato][orc] = prato_ant;
                    }
                }
            }
        }
        
        // Busca situacao (prato) com melhor lucro no ultima dia.
        // Se tiver mais de um com maior lucro, pegar o prato com
        // menor custo
        int p = 0;
        for (int p_aux = 1; p_aux < n; p_aux++) {
            if (dp[k - 1][p_aux][m] > dp[k - 1][p][m]) {
                p = p_aux;
            } else if (dp[k - 1][p_aux][m] == dp[k - 1][p][m]) {
                p = custos[p_aux] < custos[p] ? p_aux : p;
            }
        }

        if (dp[k - 1][p][m] == -1) {
            cout << "0.0" << endl;
        } else {
            cout << fixed;
            cout << setprecision(1);
            cout << dp[k - 1][p][m] << endl;
            cout << p + 1 << " ";

            int dia = k - 1;
            int orc = m;      
            int p_ant = p;
            p = caminho[dia][p][orc];
            
            while (p != -1) {    
                cout << p + 1 << " ";

                dia--;
                orc -= custos[p_ant];
                p_ant = p;
                p = caminho[dia][p][orc];
            }
            cout << endl;
        }

        cout << endl;
        cin >> k >> n >> m;
    }
    return 0;
}
