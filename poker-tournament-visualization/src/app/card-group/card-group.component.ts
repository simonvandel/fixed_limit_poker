import { Component, Input, OnChanges, OnInit, SimpleChange } from '@angular/core';

@Component({
  selector: 'app-card-group',
  templateUrl: './card-group.component.html',
  styleUrls: ['./card-group.component.css']
})
export class CardGroupComponent implements OnInit, OnChanges {
  @Input() cards: string[] = [];
  cardsToShow: string[] = []

  constructor() { }

  ngOnInit(): void {
  }
  
  ngOnChanges(changes: { [property: string]: SimpleChange }): void {
    console.log("card group changes")
    console.log(JSON.stringify(changes))
    this.cardsToShow = this.cards.map(this.mapToAsset).map(this.mapToPath)
  }

  mapToAsset(card: string): string {
    const rank = card[0] == "T" ? 10 : card[0];
    const suit = card[1].toUpperCase();
    return rank + suit;
  }
  mapToPath(mapToPath: string): string {
    return `assets/cards/${mapToPath}.svg`
  }
}
