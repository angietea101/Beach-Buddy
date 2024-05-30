import discord
from csulb_course import CSULBCourse


def create_embed(course: CSULBCourse):
    """
    :param course: A CSULBCourse object
    :return: The formatted Discord embed message
    """
    embed = discord.Embed(title=f"{course.course_abr}: {course.course_name} {course.type} ({course.units})",
                          color=discord.Color.dark_blue())
    embed.add_field(name="Professor", value=f"{course.instructor}")
    embed.add_field(name="Section Number", value=f"{course.course_section}")
    embed.add_field(name="Course Number", value=f"{course.course_number}")
    embed.add_field(name="Reserved Seats", value=f"{course.reserved_cap}")
    embed.add_field(name="Open Seats", value=f"{course.open_seats}")
    embed.add_field(name="Location", value=f"{course.location}")
    embed.add_field(name="Days", value=f"{course.days}")
    embed.add_field(name="Time", value=f"{course.time}")
    embed.add_field(name="Additional Notes", value=f"{course.comment}")
    return embed


def save_notif_channel(guild_id, channel_id):
    with open('notif.txt', 'r') as file:
        lines = file.readlines()
        update_channel = []
        for line in lines:
            if line.strip():
                guild, channel = line.strip().split(',')
                if guild == str(guild_id):
                    update_channel.append(f"{guild},{channel_id}")
                else:
                    update_channel.append(line)
    with open('notif.txt', 'w') as file:
        file.writelines(update_channel)
    print("channel updated successfully")
