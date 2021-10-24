/* eslint-disable require-jsdoc */
import { Component, Input, OnChanges, OnInit, SimpleChange } from '@angular/core';
import { HandPlayer1, History, Player, PokerGame, Stage, TopLevelPlayer1 } from '../poker-game/poker-game.service';

@Component({
  selector: 'app-poker-table',
  templateUrl: './poker-table.component.html',
  styleUrls: ['./poker-table.component.css']
})
export class PokerTableComponent implements OnInit, OnChanges {
  @Input() game!: PokerGame;
  @Input() stage!: Stage;

  history: History[] = [];
  community: string[] = [];

  player1!: Player;
  player2!: Player;
  player1link="https://media-exp1.licdn.com/dms/image/C5603AQGAUW9uU9JtGw/profile-displayphoto-shrink_200_200/0/1581669563810?e=1640217600&v=beta&t=WHteJ76sNXQZ9l6yySjTvMNTyExfgZtYPa5WRIctkyk"
  player2link="https://media-exp1.licdn.com/dms/image/C5603AQHxqi2EjCLiKQ/profile-displayphoto-shrink_200_200/0/1580829910259?e=1640217600&v=beta&t=6Ry0x-EzdCjOmgaIcXGoO4jrZv7Uh2ROx2ymfOr3ag4"
  pot = 225

  constructor() {
  }

  ngOnInit(): void {
    this.player1 = this.getPlayer(this.game.hands[0].player1, this.game.player1);
    this.player2 = this.getPlayer(this.game.hands[0].player2, this.game.player2);
    this.history = this.game.hands[0].history;
  }

  ngOnChanges(changes: { [property: string]: SimpleChange }): void {
    console.log("table changes!")
    let change: SimpleChange = changes['data'];
    console.log(change)
    console.log(changes)
    this.setCommunity();
  }

  getPlayer(handPlayer: HandPlayer1, player: TopLevelPlayer1): Player {
    return {
      name: player.name,
      winner: player.winner,
      cards: handPlayer.cards,
      total_reward: player.total_reward
    }
  }

  setCommunity(): void {
    const community: string[] = []
    if (this.stage == Stage.Flop) {
      const cards = this.game.hands[0].history[this.getStageIndex(Stage.Flop)]!.board_cards;
      if (cards != undefined) {
        community.push(...cards);
      }
    }

    if (this.stage == Stage.Turn) {
      const cards = this.game.hands[0].history[this.getStageIndex(Stage.Turn)]!.board_cards;
      if (cards != undefined) {
        community.push(...cards);
      }
    }
    if (this.stage == Stage.River || this.stage == Stage.Showdown) {
      const cards = this.game.hands[0].history[this.getStageIndex(Stage.River)]!.board_cards;
      if (cards != undefined) {
        community.push(...cards);
      }
    }

    this.community = community;
  }

  getStageIndex(stage: Stage) {
    return this.history.findIndex(x => x.action == stage.toString().toLocaleLowerCase())
  }
}

