import discord
from typing import List


class PaginatorView(discord.ui.View):
    def __init__(self, embeds: List[discord.Embed]) -> None:
        super().__init__(timeout=60)
        self._embeds = embeds
        self._initial = embeds[0]
        self._current_page = 1
        self._max_page = len(embeds)
        self._initial.set_footer(text=f"Page {self._current_page}/{self._max_page}")
        # Disables the previous button at initial page
        self.children[0].disabled = True

    def get_current_embed(self):
        return self._embeds[self._current_page - 1]

    def previous_page(self):
        if self._current_page > 1:
            self._current_page -= 1
        return self.get_current_embed()

    def next_page(self):
        if self._current_page < self._max_page:
            self._current_page += 1
        return self.get_current_embed()

    async def update_buttons(self, interaction: discord.Interaction) -> None:
        for index in self._embeds:
            index.set_footer(text=f"Page {self._current_page}/{self._max_page}")

        # Disables the next button if at max page
        if self._current_page == self._max_page:
            self.children[1].disabled = True
        else:
            self.children[1].disabled = False

        # Disables the previous button if at first page
        if self._current_page == 1:
            self.children[0].disabled = True
        else:
            self.children[0].disabled = False

        await interaction.message.edit(view=self)

    @discord.ui.button(style=discord.ButtonStyle.danger, label="PREVIOUS")
    async def previous(self, interaction: discord.Interaction, _):
        embed = self.previous_page()
        await self.update_buttons(interaction)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(style=discord.ButtonStyle.success, label="NEXT")
    async def next(self, interaction: discord.Interaction, _):
        embed = self.next_page()
        await self.update_buttons(interaction)
        await interaction.response.edit_message(embed=embed, view=self)
