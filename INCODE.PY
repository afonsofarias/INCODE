{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOYpe279BxXAAH9w6sAV2g/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/afonsofarias/INCODE/blob/main/INCODE.PY\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **INCODE - AULA - 2**"
      ],
      "metadata": {
        "id": "vROVz2-51PXZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Soma de 2 numeros**"
      ],
      "metadata": {
        "id": "B__tsG-b3O9w"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mm6xdU1I7r38",
        "outputId": "c1eb9404-8cf3-4956-aed0-80724b7852ec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro numero: 3\n",
            "Digite o segundo numero: 4\n",
            "a soma é: 7.0\n"
          ]
        }
      ],
      "source": [
        "n1 = float(input(\"Digite o primeiro numero: \"))\n",
        "n2 = float(input(\"Digite o segundo numero: \"))\n",
        "resultado = n1+n2\n",
        "print(f\"a soma é: {resultado}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Media de escolar**"
      ],
      "metadata": {
        "id": "KtvXAuTh3Uc5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n1 = float(input(\"Digite a primeira nota: \"))\n",
        "n2 = float(input(\"Digite o segunda nota: \"))\n",
        "m = (n1+n2)/2\n",
        "print(f\"a media é é: {m:.1f}\")"
      ],
      "metadata": {
        "id": "S9xuVh6579r8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Verifica maior, menor ou igualdade**"
      ],
      "metadata": {
        "id": "MujgbdqY3eLw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n1 = float(input(\"insira o primeiro numero: \"))\n",
        "n2 = float(input(\"insira o primeiro numero: \"))\n",
        "if(n1>n2):\n",
        "  print(\"n1 é maior que n2\")\n",
        "elif(n1==n2):\n",
        "  print(\"n1 e n2 sao iguais\")\n",
        "else:\n",
        "  print(\"n2 é maior que n1\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wZQpZqmGBCK3",
        "outputId": "b21f3ec8-a1c8-4bcb-8f2b-eaa35e1c25b4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "insira o primeiro numero: 4\n",
            "insira o primeiro numero: 6\n",
            "n2 é maior que n14\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Diferente de zero**"
      ],
      "metadata": {
        "id": "uYmm2PdH3mOh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n1 = float(input(\"insira um numero: \"))\n",
        "if(n1>0):\n",
        "  print(\"n1 é positivo\")\n",
        "elif(n1==0):\n",
        "  print(\"n1 é zero\")\n",
        "else:\n",
        "  print(\"n1 é negativo\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2uTayaEcMbnJ",
        "outputId": "902c601c-7073-4ef9-ecdc-01fb047ebb85"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "insira um numero: 0\n",
            "n1 é zero\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **BEECROWD - LISTA 2 - INCODE**"
      ],
      "metadata": {
        "id": "27Vgjt-42Mro"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**BEECROWD - \t1037\tIntervalo**"
      ],
      "metadata": {
        "id": "GwGGmHxC1iji"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "v = float(input())\n",
        "\n",
        "if (v >= 0 and v < 25.01):\n",
        "  print(\"Intervalo [0,25]\")\n",
        "\n",
        "elif(v >= 25.01 and v < 50.01):\n",
        "  print(\"Intervalo (25,50]\")\n",
        "\n",
        "elif(v >= 50.01 and v < 75.01):\n",
        "  print(\"Intervalo (50,75]\")\n",
        "\n",
        "elif(v >= 75.01 and v <= 100.00):\n",
        "  print(\"Intervalo (75,100]\")\n",
        "\n",
        "else:\n",
        "  print(\"Fora de intervalo\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N-Neoc722K4Q",
        "outputId": "164a6812-fc19-4fcd-cb4f-5538d917c0ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "36.5\n",
            "Intervalo (25,50]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**BEECROWD - 1038 Lanche**"
      ],
      "metadata": {
        "id": "cjQ5l4Bj1_KB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "C, Q = map(int,input().split())\n",
        "\n",
        "if(C == 1):\n",
        "    V = Q * (4.00)\n",
        "    print(f\"Total: R$ {V:.2f}\")\n",
        "elif(C == 2):\n",
        "    V = Q * (4.50)\n",
        "    print(f\"Total: R$ {V:.2f}\")\n",
        "elif(C == 3):\n",
        "    V = Q * (5.00)\n",
        "    print(f\"Total: R$ {V:.2f}\")\n",
        "elif(C == 4):\n",
        "    V = Q * (2.00)\n",
        "    print(f\"Total: R$ {V:.2f}\")\n",
        "elif(C == 5):\n",
        "    V = Q * (1.50)\n",
        "    print(f\"Total: R$ {V:.2f}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4TbucLIM2Jrv",
        "outputId": "80ec03b7-00d0-4754-d188-02b89101eb99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 3\n",
            "Total: R$ 12.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**BEECROWD - 1044 Múltiplos**"
      ],
      "metadata": {
        "id": "Zsf9c6so01Fh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A, B = map(int,input().split())\n",
        "print(type(A))\n",
        "print(type(B))\n",
        "print(type(A%B==0))\n",
        "print(type(B%A==0))\n",
        "if (A%B==0 or B%A==0):\n",
        "    print(\"Sao Multiplos\")\n",
        "else:\n",
        "    print(\"Nao sao Multiplos\")"
      ],
      "metadata": {
        "id": "oce3C3KN0Qe6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**BEECROWD - 1046 Tempo de Jogo**"
      ],
      "metadata": {
        "id": "UbknhGit2rVA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "I, F = map(int,input().split())\n",
        "DIA=int(24)\n",
        "\n",
        "if(I>F):\n",
        "    DUR=((DIA-I)+F)\n",
        "    print(f\"O JOGO DUROU {DUR} HORA(S)\")\n",
        "elif(I==F):\n",
        "    DUR=24\n",
        "    print(f\"O JOGO DUROU {DUR} HORA(S)\")\n",
        "else:\n",
        "    DUR=F-I\n",
        "    print(f\"O JOGO DUROU {DUR} HORA(S)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mdcfzGcC2sRY",
        "outputId": "0717c389-0bc0-4fa1-e77a-cd34d0459351"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**BEECROWD - 1050 DDD**"
      ],
      "metadata": {
        "id": "qDmtlZnK2z4w"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ddd = int(input())\n",
        "\n",
        "if(ddd==61):\n",
        "    print(\"Brasilia\")\n",
        "elif(ddd==71):\n",
        "    print(\"Salvador\")\n",
        "elif(ddd==11):\n",
        "    print(\"Sao Paulo\")\n",
        "elif(ddd==21):\n",
        "    print(\"Rio de Janeiro\")\n",
        "elif(ddd==32):\n",
        "    print(\"Juiz de Fora\")\n",
        "elif(ddd==19):\n",
        "    print(\"Campinas\")\n",
        "elif(ddd==27):\n",
        "    print(\"Vitoria\")\n",
        "elif(ddd==31):\n",
        "    print(\"Belo Horizonte\")\n",
        "else:\n",
        "    print(\"DDD nao cadastrado\")"
      ],
      "metadata": {
        "id": "mfRy0elo26oQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**BEECROWD - 1051 Imposto de Renda**"
      ],
      "metadata": {
        "id": "32D4ZCNg2-Rv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "salario = float(input())\n",
        "\n",
        "if(salario<=2000):\n",
        "    print(\"Isento\")\n",
        "elif(salario>2000 and salario<=3000):\n",
        "    imposto=(salario-2000)*0.08\n",
        "    print(f\"R$ {imposto:.2f}\")\n",
        "elif(salario>3000 and salario<=4500):\n",
        "    imposto=((salario-3000)*0.18)+80\n",
        "    print(f\"R$ {imposto:.2f}\")\n",
        "else:\n",
        "    imposto=((salario-4500)*0.28)+350\n",
        "    print(f\"R$ {imposto:.2f}\")"
      ],
      "metadata": {
        "id": "dUSuoPxh3GAC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0f5fa0f2-7aa7-4347-c378-38aee717563d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15900\n",
            "R$ 3542.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**BEECROWD - 1010 CÁLCULO SIMPLES**"
      ],
      "metadata": {
        "id": "YEI4sV-WbPSk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "COD1, QTD1, VAL1 = map(float, input().split())\n",
        "COD2, QTD2, VAL2 = map(float, input().split())\n",
        "\n",
        "TOTAL = (QTD1 * VAL1) + (QTD2 * VAL2)\n",
        "\n",
        "print(f\"VALOR A PAGAR: R$ {TOTAL:.2f}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ienNVOZwbcu7",
        "outputId": "fed44087-5d28-4ba1-f929-017b48f97f63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12 1 5.30\n",
            "16 2 5.10\n",
            "VALOR A PAGAR: R$ 15.50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**BEECROWD INICIANTE**"
      ],
      "metadata": {
        "id": "S7Ww3Ynchbby"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**BEECROWD - 1011 ESFERA**"
      ],
      "metadata": {
        "id": "H3Zps0eXdU3e"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "R = float(input())\n",
        "V = ((4/3.0) * (3.14159 * (R**3)))\n",
        "print(f'VOLUME = {V:.3F}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oxKz_pphddcb",
        "outputId": "8fa6185a-bb91-46b7-f156-f8543dcfba03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "16\n",
            "VOLUME = 17157.270\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**BEECROWD - 1012 ÁREA**"
      ],
      "metadata": {
        "id": "5EdENTnNe29t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a, b, c = map(float, input().split())\n",
        "\n",
        "print(f'TRIANGULO: {((a * c) / 2):.3f}')\n",
        "print(f'CIRCULO: {(3.14159 * (c**2)):.3f}')\n",
        "print(f'TRAPEZIO: {(((a + b) * c) / 2):.3f}')\n",
        "print(f'QUADRADO: {(b**2):.3f}')\n",
        "print(f'RETANGULO: {(a * b):.3f}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MlP0iRhIfDkC",
        "outputId": "5c2e2649-8ca1-4127-bac2-9b88ec0c4c2f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15 15 15\n",
            "triangulo: 112.500\n",
            "circulo: 706.858\n",
            "trapezio: 225.000\n",
            "quadrado: 225.000\n",
            "retangulo: 225.000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**BEECROWD - 1013 O MAIOR**"
      ],
      "metadata": {
        "id": "62142umbpR9c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A,B,C=list(map(int,input().split()))\n",
        "print(\"{} eh o maior\".format(max(A,B,C)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EImQP83WpZtc",
        "outputId": "4eff88d5-01a4-4948-d7a3-581aabecfa06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n",
            "3 eh o maior\n"
          ]
        }
      ]
    }
  ]
}