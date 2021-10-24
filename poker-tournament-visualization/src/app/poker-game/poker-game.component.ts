import { Component, OnChanges, OnInit, Output } from '@angular/core';
import {
  PokerGame,
  PokerGameService,
  Stage,
  History,
} from './poker-game.service';

@Component({
  selector: 'app-poker-game',
  templateUrl: './poker-game.component.html',
  styleUrls: ['./poker-game.component.css'],
})
export class PokerGameComponent implements OnInit, OnChanges {
  game: PokerGame;
  stage: Stage;
  actionSlider: number = 1;
  timeLeft: number = 60;
  interval: any;

  constructor(private pokerGameService: PokerGameService) {
    this.game = this.pokerGameService.game[0];
    this.stage = Stage.Preflop;
  }

  ngOnInit(): void {}

  ngOnChanges(): void {
    console.log('game changes!');
    this.setStage();
  }

  playPause(): void {
    console.log('pause / play');
    // Pause if playing
    if (this.interval != null) {
      console.log('pausing');
      clearInterval(this.interval);
      return;
    }
    // Start playing.
    console.log('playing');
    this.interval = setInterval(() => {
      console.log('play loop');
      if (this.actionSlider < this.getMaxActions()) {
        this.actionSlider = this.actionSlider + 1;
          this.sliderOnChange(this.actionSlider + 1);
      } else {
        if (this.interval != null) {
          clearInterval(this.interval);
        }
      }
    }, 1000);
  }

  setStage(val?: number): void {
    const newValue = val ? val : this.actionSlider;
    let currentStage = Stage.Preflop;
    for (let index = 0; index <= newValue; index++) {
      const action = this.game.hands[0].history[index].action;
      if (action == Stage.Preflop) {
        currentStage = Stage.Preflop;
      } else if (action == Stage.Flop) {
        currentStage = Stage.Flop;
      } else if (action == Stage.Turn) {
        currentStage = Stage.Turn;
      } else if (action == Stage.River) {
        currentStage = Stage.River;
      }
    }
    this.stage = currentStage;
  }

  getMaxActions(): number {
    const actions = this.game.hands[0].history.length;
    return actions; // +1 for the show-down
  }

  getCurrentAction(): History {
    const idx = this.actionSlider;
    return this.game.hands[0].history[idx];
  }

  sliderOnChange(event: any) {
    this.setStage(event.value);
  }
}
