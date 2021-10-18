import { Injectable } from '@angular/core';


export interface Player {
  cards: string[];
  name: string;
  total_reward: number;
  winner?: boolean;
}

export interface PokerGame {
  game_nbr: number;
  tournament_stage: number;
  player1: TopLevelPlayer1;
  player2: TopLevelPlayer1;
  hands: Hand[];
  winner?: string;
}

export interface Hand {
  nbr: number;
  raise_count: number;
  abs_reward: number;
  player1: HandPlayer1;
  player2: HandPlayer1;
  history: History[];
  player1_total_reward_before?: number;
  player2_total_reward_before?: number;
  winner?: string;
}

export interface History {
  player?: string;
  action: string;
  total_player_contribution?: number;
  board_cards?: string[];
}

export interface HandPlayer1 {
  total_reward_before: number;
  winner: boolean;
  cards: string[];
}

export interface TopLevelPlayer1 {
  name: string;
  total_reward: number;
  winner?: boolean;
}

export enum Stage {
  Preflop = "preflop",
  Flop = "flop",
  Turn = "turn",
  River = "river",
  Showdown = "showdown"
}

@Injectable({
  providedIn: 'root'
})
export class PokerGameService {
  game: PokerGame[];

  constructor() {
    this.game = [
      {
        "game_nbr": 1,
        "tournament_stage": 16,
        "player1": {
          "name": "nc_frederik",
          "total_reward": 100,
          "winner": true
        },
        "player2": {
          "name": "nc_jakob",
          "total_reward": -100,
          "winner": false
        },
        "hands": [
          {
            "nbr": 1,
            "raise_count": 3,
            "abs_reward": 50,
            "player1": {
              "total_reward_before": 0,
              "winner": false,
              "cards": [
                "Th",
                "Ad"
              ]
            },
            "player2": {
              "total_reward_before": 0,
              "winner": true,
              "cards": [
                "9h",
                "8h"
              ]
            },
            "history": [
              {
                "player": "player1",
                "action": "small_blind",
                "total_player_contribution": 5
              },
              {
                "player": "player2",
                "action": "big_blind",
                "total_player_contribution": 10
              },
              {
                "player": "player1",
                "action": "call",
                "total_player_contribution": 10
              },
              {
                "player": "player2",
                "action": "check",
                "total_player_contribution": 10
              },
              {
                "action": "flop",
                "board_cards": [
                  "3h",
                  "Qh",
                  "5h"
                ]
              },
              {
                "player": "player1",
                "action": "check",
                "total_player_contribution": 10
              },
              {
                "player": "player2",
                "action": "raise",
                "total_player_contribution": 20
              },
              {
                "player": "player1",
                "action": "raise",
                "total_player_contribution": 30
              },
              {
                "player": "player2",
                "action": "call",
                "total_player_contribution": 30
              },
              {
                "action": "turn",
                "board_cards": [
                  "3h",
                  "Qh",
                  "5h",
                  "Ac"
                ]
              },
              {
                "player": "player1",
                "action": "raise",
                "total_player_contribution": 50
              },
              {
                "player": "player2",
                "action": "call",
                "total_player_contribution": 50
              },
              {
                "action": "river",
                "board_cards": [
                  "3h",
                  "Qh",
                  "5h",
                  "Ac",
                  "Jd"
                ]
              },
              {
                "player": "player1",
                "action": "check",
                "total_player_contribution": 50
              },
              {
                "player": "player2",
                "action": "check",
                "total_player_contribution": 50
              }
            ]
          }
        ]
      },
      {
        "game_nbr": 2,
        "tournament_stage": 16,
        "player1": {
          "name": "nc_troels",
          "total_reward": 400
        },
        "player2": {
          "name": "nc_martin",
          "total_reward": -400
        },
        "winner": "player1",
        "hands": []
      }
    ]
  }
}
